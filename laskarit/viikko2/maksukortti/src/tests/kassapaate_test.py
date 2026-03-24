from kassapaate import Kassapaate
from maksukortti import Maksukortti

def test_alku_oikein():
    kassa = Kassapaate()

    assert kassa.kassassa_rahaa == 100000
    assert kassa.edulliset == 0
    assert kassa.maukkaat == 0


def test_kateinen_onnistuu():
    kassa = Kassapaate()
    vaihtoraha = kassa.syo_edullisesti_kateisella(300)

    assert vaihtoraha == 60
    assert kassa.kassassa_rahaa == 100000 + 240
    assert kassa.edulliset == 1


def test_kateinen_ei_riita():
    kassa = Kassapaate()
    vaihtoraha = kassa.syo_edullisesti_kateisella(200)

    assert vaihtoraha == 200
    assert kassa.kassassa_rahaa == 100000
    assert kassa.edulliset == 0


def test_maukas_kateinen_onnistuu():
    kassa = Kassapaate()
    vaihtoraha = kassa.syo_maukkaasti_kateisella(500)

    assert vaihtoraha == 100
    assert kassa.kassassa_rahaa == 100000 + 400
    assert kassa.maukkaat == 1


def test_maukas_kateinen_ei_riita():
    kassa = Kassapaate()
    vaihtoraha = kassa.syo_maukkaasti_kateisella(300)

    assert vaihtoraha == 300
    assert kassa.kassassa_rahaa == 100000
    assert kassa.maukkaat == 0


def test_edullinen_kortti_onnistuu():
    kassa = Kassapaate()
    kortti = Maksukortti(1000)

    onnistui = kassa.syo_edullisesti_kortilla(kortti)

    assert onnistui is True
    assert kortti.saldo == 1000 - 240
    assert kassa.edulliset == 1
    assert kassa.kassassa_rahaa == 100000


def test_edullinen_kortti_ei_riita():
    kassa = Kassapaate()
    kortti = Maksukortti(100)

    onnistui = kassa.syo_edullisesti_kortilla(kortti)

    assert onnistui is False
    assert kortti.saldo == 100
    assert kassa.edulliset == 0
    assert kassa.kassassa_rahaa == 100000


def test_kortti_onnistuu():
    kassa = Kassapaate()
    kortti = Maksukortti(1000)

    onnistui = kassa.syo_maukkaasti_kortilla(kortti)

    assert onnistui is True
    assert kortti.saldo == 1000 - 400
    assert kassa.maukkaat == 1
    assert kassa.kassassa_rahaa == 100000


def test_kortti_ei_riita():
    kassa = Kassapaate()
    kortti = Maksukortti(100)

    onnistui = kassa.syo_maukkaasti_kortilla(kortti)

    assert onnistui is False
    assert kortti.saldo == 100
    assert kassa.maukkaat == 0
    assert kassa.kassassa_rahaa == 100000


def test_lataus_kortille():
    kassa = Kassapaate()
    kortti = Maksukortti(1000)

    kassa.lataa_rahaa_kortille(kortti, 500)

    assert kortti.saldo == 1500
    assert kassa.kassassa_rahaa == 100000 + 500


def test_negatiivinen_lataus_ei_muuta():
    kassa = Kassapaate()
    kortti = Maksukortti(1000)

    kassa.lataa_rahaa_kortille(kortti, -500)

    assert kortti.saldo == 1000
    assert kassa.kassassa_rahaa == 100000