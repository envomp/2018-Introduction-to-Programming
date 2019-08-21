import pytest
from ex04_cipher import encode, decode


@pytest.mark.timeout(1.0)
def test_encode_key_1():
    assert encode("hello", 1) == "hello"


@pytest.mark.timeout(1.0)
def test_encode_longer_sentence_key_1():
    assert encode("mul pole tuju", 1) == "mul_pole_tuju"


@pytest.mark.timeout(1.0)
def test_encode_sentence_key_2():
    assert encode("ma kodeerin", 2) == "m_oernakdei"


@pytest.mark.timeout(1.0)
def test_encode_sentence_key_3():
    assert encode("palun kodeeri mind", 3) == "pndinau_oer_idlkem"


@pytest.mark.timeout(1.0)
def test_encode_key_bigger_than_length():
    assert encode("kodeerimine", 15) == "kodeerimine"


@pytest.mark.timeout(1.0)
def test_encode_sentence_letter_sensitive():
    assert encode("SUUR Ja small", 4) == "SalUJ_lU_saRm"


@pytest.mark.timeout(1.0)
def test_encode_sentence_hard():
    assert encode("Raskus on ainult in key value", 7) == "Rnvaiu_asalylk_teuun_kesoi__n"


@pytest.mark.timeout(1.0)
def test_encode_sentence_key_bigger_than_length():
    assert encode("ma ei taha", 15) == "ma_ei_taha"


@pytest.mark.timeout(1.0)
def test_decode_key_1():
    assert decode("hello", 1) == "hello"


@pytest.mark.timeout(1.0)
def test_decode_longer_sentence_key_1():
    assert decode("mul_pole_tuju", 1) == "mul pole tuju"


@pytest.mark.timeout(1.0)
def test_decode_sentence_key_2():
    assert decode("m_oernakdei", 2) == "ma kodeerin"


@pytest.mark.timeout(1.0)
def test_decode_sentence_key_3():
    assert decode("pndinau_oer_idlkem", 3) == "palun kodeeri mind"


@pytest.mark.timeout(1.0)
def test_decode_key_bigger_than_length():
    assert decode("kodeerimine", 15) == "kodeerimine"


@pytest.mark.timeout(1.0)
def test_decode_sentence_key_bigger_than_length():
    assert decode("ma_ei_taha", 15) == "ma ei taha"


@pytest.mark.timeout(1.0)
def test_decode_sentence_letter_sensitive():
    assert decode("SalUJ_lU_saRm", 4) == "SUUR Ja small"
