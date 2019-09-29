from unittest import TestCase

from GeneradorEstadisticas import GeneradorEstadisticas


class TestGeneradorEstadisticas(TestCase):
    def test_calcular_numero_elementos_cadena_vacia(self):
        self.assertEqual(GeneradorEstadisticas().calcular(""), [0], "numero elementos con cadena vacia")
