import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()

    def test_kassassa_rahaa_alussa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_edullisten_maara_alussa_nolla(self):
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukkaiden_maara_alussa_nolla(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_kateisella_kasvattaa_kassaa(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_kateisella_ei_riittava_raha(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_edullinen_kortilla_onnistuu(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 760)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_kortilla_ei_riittava_saldo(self):
        kortti = Maksukortti(200)
        onnistui = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukas_kortilla_onnistuu(self):
        kortti = Maksukortti(1000)
        onnistui = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertTrue(onnistui)
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukas_kortilla_ei_riittava_saldo(self):
        kortti = Maksukortti(300)
        onnistui = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 300)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_rahan_lataaminen_kortille_kasvattaa_saldoa(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, 500)

        self.assertEqual(kortti.saldo, 1500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)

    def test_negatiivinen_lataus_ei_muuta_tilannetta(self):
        kortti = Maksukortti(1000)
        self.kassa.lataa_rahaa_kortille(kortti, -500)

        self.assertEqual(kortti.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)