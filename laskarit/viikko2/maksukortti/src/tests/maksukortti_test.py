import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")


    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo_euroina(), 7.5)

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti=Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)

    def test_syo_maukkaasti_ei_vie_saldo_negatiiviseksi(self):
	    kortti=Maksukortti(300)
	    kortti.syo_maukkaasti()

	    self.assertEqual(kortti.saldo_euroina(), 3.0)

    def test_kortille_voi_ladata_rahaa(self):
    	self.kortti.lataa_rahaa(2500)

    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
    	self.kortti.lataa_rahaa(20000)

    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

    def test_negatiivinen_summan_lataaminen_ei_muuta_kortin_arvoa(self):
	    self.kortti.lataa_rahaa(-1500)

	    self.assertEqual(self.kortti.saldo_euroina(), 10)

    def test_voi_syoda_edullisesti_kun_saldo_on_250(self):
        kortti=Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 0)

    def test_voi_syoda_maukaasti_kun_saldo_on_400(self):
        kortti=Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 0)
