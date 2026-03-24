from maksukortti import Maksukortti

def test_konstruktori_asettaa_saldon_oikein():
    kortti = Maksukortti(1000)
    assert str(kortti) == "Kortilla on rahaa 10.00 euroa"

def test_syo_edullisesti_vahentaa_saldoa_oikein():
    kortti = Maksukortti(1000)
    kortti.syo_edullisesti()
    assert kortti.saldo_euroina() == 7.5

def test_syo_maukkaasti_vahentaa_saldoa_oikein():
    kortti = Maksukortti(1000)
    kortti.syo_maukkaasti()
    assert kortti.saldo_euroina() == 6.0

def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi():
    kortti = Maksukortti(200)
    kortti.syo_edullisesti()
    assert kortti.saldo_euroina() == 2.0

def test_kortille_voi_ladata_rahaa():
    kortti = Maksukortti(1000)
    kortti.lataa_rahaa(2500)
    assert kortti.saldo_euroina() == 35.0

def test_kortin_saldo_ei_ylita_maksimiarvoa():
    kortti = Maksukortti(1000)
    kortti.lataa_rahaa(20000)
    assert kortti.saldo_euroina() == 150.0

def test_negatiivinen_lataus_ei_muuta_saldoa():
    kortti = Maksukortti(1000)
    kortti.lataa_rahaa(-500)
    assert kortti.saldo_euroina() == 10.0