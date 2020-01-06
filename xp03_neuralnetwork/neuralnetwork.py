"""Neural network. Push again. Try again."""

import torch
from torchvision import models, transforms
import torch.utils.data
import torch.nn as nn
import torch.optim as optim
from PIL import Image


normalize_transform = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomRotation(30),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        normalize_transform
    ]),
    'eval': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        normalize_transform
    ])
}


class ImageClassifier:
    """Image classifier class........."""

    def __init__(self, device, class_count: int):
        """Initialize classifier instance."""
        self._device = device
        self._model = None
        self._optimizer = None
        self._criterion = nn.CrossEntropyLoss()
        self._class_count = class_count

    def create(self):
        """Create pre-trained model."""
        self._model = models.resnet50(pretrained=True).to(self._device)

        for param in self._model.parameters():
            param.requires_grad = False

        self._model.fc = nn.Sequential(
            nn.Linear(self._model.fc.in_features, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, self._class_count)
        ).to(self._device)

        self._optimizer = optim.Adam(self._model.fc.parameters())

    def save(self, file_path: str):
        """Save model."""
        torch.save(self._model.state_dict(), file_path)

    def load(self, file_path: str):
        """Load model."""
        self._model = models.resnet50(pretrained=False).to(self._device)

        self._model.fc = nn.Sequential(
            nn.Linear(self._model.fc.in_features, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, self._class_count)
        ).to(self._device)

        self._model.load_state_dict(torch.load(file_path, map_location=self._device))
        self._optimizer = optim.Adam(self._model.fc.parameters())

    def _train(self, data_loader) -> (float, float):
        """Training procedure."""
        self._model.train()
        running_loss = 0.0
        running_corrects = 0.0

        for inputs, labels in data_loader:
            inputs = inputs.to(self._device)
            labels = labels.to(self._device)

            self._optimizer.zero_grad()
            outputs = self._model(inputs)
            loss = self._criterion(outputs, labels)
            loss.backward()
            self._optimizer.step()

            result = torch.max(outputs, 1)
            running_loss += loss.detach() * inputs.size(0)
            running_corrects += torch.sum(result.indices == labels.data).float()

        running_loss /= len(data_loader.dataset)
        running_corrects /= len(data_loader.dataset)
        return running_loss, running_corrects

    def _eval(self, data_loader) -> (float, float):
        """Evaluate procedure."""
        self._model.eval()
        running_loss = 0.0
        running_corrects = 0.0

        for inputs, labels in data_loader:
            inputs = inputs.to(self._device)
            labels = labels.to(self._device)

            outputs = self._model(inputs)
            loss = self._criterion(outputs, labels)

            result = torch.max(outputs, 1)
            running_loss += loss.detach() * inputs.size(0)
            running_corrects += torch.sum(result.indices == labels.data).float()

        running_loss /= len(data_loader.dataset)
        running_corrects /= len(data_loader.dataset)
        return running_loss, running_corrects

    def train(self, train_loader, eval_loader, num_epochs=3):
        """Train model."""
        for epoch in range(num_epochs):
            print(f"Epoch {epoch + 1}/{num_epochs}")
            print('-' * 10)
            epoch_loss, epoch_acc = self._train(train_loader)
            print(f"Training loss: {epoch_loss:.4f}, accuracy: {epoch_acc:.4f}")
            epoch_loss, epoch_acc = self._eval(eval_loader)
            print(f"Validation loss: {epoch_loss:.4f}, accuracy: {epoch_acc:.4f}\n")

    def predict_one(self, image_path: str) -> int:
        """Guess single image."""
        self._model.eval()
        img = Image.open(image_path)
        data = data_transforms['eval'](img).to(self._device).float().unsqueeze(0)
        prediction_tensor = self._model(data)
        result = torch.max(prediction_tensor, 1)
        return result.indices[0]


def guess_animal(image_path: str) -> str:
    """
    Read the image file and guess the animal.

    :param image_path: Path to the image
    :return: Animal species as string
    """
    labels = ("cat", "giraffe", "rabbit")
    return labels[guess_animal.classifier.predict_one(image_path)]


guess_animal.classifier = ImageClassifier("cpu", 3)
guess_animal.classifier.load('neuralnetwork.pth')


if __name__ == '__main__':
    """
    from torchvision import datasets

    train_dir = './images/training'
    valid_dir = './images/validation'

    image_datasets = {
        'train': datasets.ImageFolder(train_dir, transform=data_transforms['train']),
        'eval': datasets.ImageFolder(valid_dir, transform=data_transforms['eval'])
    }

    data_loaders = {
        'train': torch.utils.data.DataLoader(image_datasets['train'], batch_size=64, shuffle=True),  # num_workers
        'eval': torch.utils.data.DataLoader(image_datasets['eval'], batch_size=32),
    }

    ic = ImageClassifier("cuda:0" if torch.cuda.is_available() else "cpu", len(image_datasets['train'].classes))
    ic.load('./neuralnetwork.py')
    ic.train(data_loaders['train'], data_loaders['eval'], 3)
    ic.save('./neuralnetwork_.pth')
    """

    print(guess_animal("./toy-rabbit.jpg"))
    print(guess_animal("./toy-cat.jpg"))
    print(guess_animal("./toy-giraffe.jpg"))
