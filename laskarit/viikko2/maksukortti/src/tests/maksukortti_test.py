from maksukortti import Maksukortti

def test_saldo_alussa():
    kortti = Maksukortti(1000)
    assert kortti.saldo == 1000

def test_lataaminen():
    kortti = Maksukortti(1000)
    kortti.lataa_rahaa(500)
    assert kortti.saldo == 1500

def test_saldo_vahenee():
    kortti = Maksukortti(1000)
    onnistui = kortti.ota_rahaa(200)

    assert onnistui is True
    assert kortti.saldo == 800

def test_saldo_ei_muutu():
    kortti = Maksukortti(1000)
    onnistui = kortti.ota_rahaa(2000)

    assert onnistui is False
    assert kortti.saldo == 1000

def test_negatiivinen_lataus():
    kortti = Maksukortti(1000)
    kortti.lataa_rahaa(-100)
    assert kortti.saldo == 1000

def test_saldoei_maksimi():
    kortti = Maksukortti(14000)
    kortti.lataa_rahaa(2000)
    assert kortti.saldo == 15000

def test_syo_edullisesti():
    kortti = Maksukortti(1000)
    kortti.syo_edullisesti()

    assert kortti.saldo == 760

def test_syo_edullisesti_ei_onnistu():
    kortti = Maksukortti(100)
    kortti.syo_edullisesti()

    assert kortti.saldo == 100

def test_syo_maukkaasti_ei_onnistu():
    kortti = Maksukortti(100)
    kortti.syo_maukkaasti()

    assert kortti.saldo == 100