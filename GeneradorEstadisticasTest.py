from unittest import TestCase

from GeneradorEstadisticas import GeneradorEstadisticas


class TestGeneradorEstadisticas(TestCase):

    def test_calcular_minimo_y_numero_elementos_cadena_vacia(self):
        self.assertEqual(GeneradorEstadisticas().calcular(""), [0], "minimo con cadena vacia")

    def test_calcular_minimo_con_un_numero(self):
        self.assertEqual(GeneradorEstadisticas().calcular("5"), [1,5], "minimo con cadena un numero")

    def test_calcular_minimo_con_dos_numeros(self):
        self.assertEqual(GeneradorEstadisticas().calcular("5,2"), [2,2], "minimo con cadena dos numeros")

    def test_calcular_minimo_con_n_numeros(self):
        self.assertEqual(GeneradorEstadisticas().calcular("5,2,4,1"), [4,1], "minimo con cadena n numeros")