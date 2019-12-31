"""
XP03 - Neural network.

Functions train(), process_image(), predict() and show_image()
are taken (and modified) from https://towardsdatascience.com
A Beginner’s Tutorial on Building an AI Image Classifier using PyTorch
"""
import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import logging


def train(pic_folder: str, model_name: str):
    """
    Train model.

    :param pic_folder:
    :param model_name: new model name
    :return: None
    """
    # Specify transforms using torchvision.transforms as transforms library
    transformations = transforms.Compose([
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    train_set = datasets.ImageFolder(pic_folder, transform=transformations)
    val_set = datasets.ImageFolder(pic_folder, transform=transformations)

    # Put into a Dataloader using torch library
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=32, shuffle=True)
    val_loader = torch.utils.data.DataLoader(val_set, batch_size=32, shuffle=True)

    # Get pretrained model using torchvision.models as models library
    model = models.densenet161(pretrained=True)

    # Turn off training for their parameters
    for param in model.parameters():
        param.requires_grad = False

    # Create new classifier for model using torch.nn as nn library
    classifier_input = model.classifier.in_features
    num_labels = 3
    classifier = nn.Sequential(nn.Linear(classifier_input, 1024),
                               nn.ReLU(),
                               nn.Linear(1024, 512),
                               nn.ReLU(),
                               nn.Linear(512, num_labels),
                               nn.LogSoftmax(dim=1))
    # Replace default classifier with new classifier
    model.classifier = classifier

    # Find the device available to use using torch library
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # Move model to the device specified above
    model.to(device)

    # Set the error function using torch.nn as nn library
    criterion = nn.NLLLoss()
    # Set the optimizer function using torch.optim as optim library
    optimizer = optim.Adam(model.classifier.parameters())
    # Load in each dataset and apply transformations using the torchvision.datasets as datasets library

    epochs = 10
    for epoch in range(epochs):
        train_loss = 0
        val_loss = 0
        accuracy = 0

        # Training the model
        model.train()
        counter = 0
        for inputs, labels in train_loader:
            # Move to device
            inputs, labels = inputs.to(device), labels.to(device)
            # Clear optimizers
            optimizer.zero_grad()
            # Forward pass
            output = model.forward(inputs)
            # Loss
            loss = criterion(output, labels)
            # Calculate gradients (backpropogation)
            loss.backward()
            # Adjust parameters based on gradients
            optimizer.step()
            # Add the loss to the training set's rnning loss
            train_loss += loss.item() * inputs.size(0)

            # Print the progress of our training
            counter += 1
            print(counter, "/", len(train_loader))

        # Evaluating the model
        model.eval()
        counter = 0
        # Tell torch not to calculate gradients
        with torch.no_grad():
            for inputs, labels in val_loader:
                # Move to device
                inputs, labels = inputs.to(device), labels.to(device)
                # Forward pass
                output = model.forward(inputs)
                # Calculate Loss
                valloss = criterion(output, labels)
                # Add loss to the validation set's running loss
                val_loss += valloss.item() * inputs.size(0)

                # Since our model outputs a LogSoftmax, find the real
                # percentages by reversing the log function
                output = torch.exp(output)
                # Get the top class of the output
                top_p, top_class = output.topk(1, dim=1)
                # See how many of the classes were correct?
                equals = top_class == labels.view(*top_class.shape)
                # Calculate the mean (get the accuracy for this batch)
                # and add it to the running accuracy for this epoch
                accuracy += torch.mean(equals.type(torch.FloatTensor)).item()

                # Print the progress of our evaluation
                counter += 1
                print(counter, "/", len(val_loader))

        # Get the average loss for the entire epoch
        train_loss = train_loss / len(train_loader.dataset)
        valid_loss = val_loss / len(val_loader.dataset)
        # Print out the information
        print('Accuracy: ', accuracy / len(val_loader))
        print('Epoch: {} \tTraining Loss: {:.6f} \tValidation Loss: {:.6f}'.format(epoch, train_loss, valid_loss))

    torch.save(model, model_name)


def process_image(image_path):
    """
    Process image.

    :param image_path: path to image
    :return: processed image
    """
    # Load Image
    img = Image.open(image_path)

    # Get the dimensions of the image
    width, height = img.size

    # Resize by keeping the aspect ratio, but changing the dimension so the shortest size is 256px
    img = img.resize((255, int(255 * (height / width))) if width < height else (int(255 * (width / height)), 255))

    # Get the dimensions of the new image size
    width, height = img.size

    # Set the coordinates to do a center crop of 224 x 224
    left = (width - 224) / 2
    top = (height - 224) / 2
    right = (width + 224) / 2
    bottom = (height + 224) / 2
    img = img.crop((left, top, right, bottom))

    # Turn image into numpy array
    img = np.array(img)

    # Make the color channel dimension first instead of last
    img = img.transpose((2, 0, 1))

    # Make all values between 0 and 1
    img = img / 255

    # Normalize based on the preset mean and standard deviation
    img[0] = (img[0] - 0.485) / 0.229
    img[1] = (img[1] - 0.456) / 0.224
    img[2] = (img[2] - 0.406) / 0.225

    # Add a fourth dimension to the beginning to indicate batch size
    img = img[np.newaxis, :]

    # Turn into a torch tensor
    image = torch.from_numpy(img)
    image = image.float()

    return image


def predict(image, model):
    """
    Using model to predict the label.

    :param image: image
    :param model: model name
    :return:
    """
    # Pass the image through our model
    output = model.forward(image)

    # Reverse the log function in our output
    output = torch.exp(output)

    # Get the top predicted class, and the output percentage for that class
    probs, classes = output.topk(1, dim=1)

    return probs.item(), classes.item()


def show_image(image):
    """
    Show image.

    :param image: Image
    :return: None
    """
    # Convert image to numpy
    image = image.numpy()

    # Un-normalize the image
    image[0] = image[0] * 0.226 + 0.445

    # To avoid logging message
    logger = logging.getLogger()
    old_level = logger.level
    logger.setLevel(100)

    # Print the image
    plt.imshow(np.transpose(image[0], (1, 2, 0)))

    # Turn logging level back
    logger.setLevel(old_level)

    plt.show()


def plot_image(path_to_image: str):
    """
    Plot image.

    :param path_to_image: path to image file
    :return: None
    """
    img = mpimg.imread(path_to_image)
    plt.imshow(img)
    plt.show()


def guess_animal1(image_path: str) -> str:
    """
    Read the image file and guess the animal.

    :param image_path: Path to the image
    :return: Animal species as string
    """
    model = torch.load("neuralnetwork.pth")
    model.eval()

    imsize = 255

    loader = transforms.Compose([
        transforms.Resize((imsize, imsize), interpolation=Image.NEAREST),
        # transforms.CenterCrop(224),
        transforms.ToTensor(),
        # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    img = Image.open(image_path)

    """
    # Proportional resize and crop
    width, height = img.size
    img = img.resize((imsize, int(imsize * (height / width))) if width < height 
                     else (int(imsize * (width / height)), imsize))
    width, height = img.size
    left = (width - 224) / 2
    top = (height - 224) / 2
    right = (width + 224) / 2
    bottom = (height + 224) / 2
    img = img.crop((left, top, right, bottom))
    """

    image = loader(img).float().unsqueeze(0)

    labels = ["cat", "giraffe", "rabbit"]
    _, index = torch.max(model(image), 1)

    return labels[index[0]]



def guess_animal(image_path: str) -> str:
    """
    Read the image file and guess the animal.

    :param image_path: Path to the image
    :return: Animal species as string
    """
    animals = ["cat", "giraffe", "rabbit"]
    model = torch.load("neuralnetwork.pth")

    image = process_image(image_path)
    top_prob, top_class = predict(image, model)

    return animals[top_class]


if __name__ == '__main__':
    # train("pics", "neuralnetwork.pth")

    path = 'test'

    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(f"{entry} - {guess_animal(os.path.join(path, entry))}")
            # plot_image(os.path.join(path, entry))

    """
    animals = ["cat", "giraffe", "rabbit"]
    model = torch.load("neuralnetwork.pth")

    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            image = process_image(os.path.join(path, entry))
            top_prob, top_class = predict(image, model)
            show_image(image)
            print(f"{entry} - {top_prob * 100} % {animals[top_class]}")
    """
