from unittest import TestCase

from GeneradorEstadisticas import GeneradorEstadisticas


class TestGeneradorEstadisticas(TestCase):
    def test_calcular_numero_elementos_cadena_vacia(self):
        self.assertEqual(GeneradorEstadisticas().calcular(""), [0], "numero elementos con cadena vacia")

    def test_calcular_numero_elementos_un_numero(self):
        self.assertEqual(GeneradorEstadisticas().calcular("8"), [1], "numero elementos con 1 numero")

    def test_calcular_numero_elementos_dos_numeros(self):
        self.assertEqual(GeneradorEstadisticas().calcular("8,5"), [2], "numero elementos con 2 numeros")

    def test_calcular_numero_elementos_n_numeros(self):
        self.assertEqual(GeneradorEstadisticas().calcular("8,5,1,4,5,3,8"), [7], "numero elementos con n numeros")

    def test_calcular_minimo_cadena_vacia(self):
        self.assertEqual(GeneradorEstadisticas().calcular(""), [0], "minimo con cadena vacia")

    def test_calcular_minimo_con_un_numero(self):
        self.assertEqual(GeneradorEstadisticas().calcular("5"), [1,5], "minimo con cadena un numero")