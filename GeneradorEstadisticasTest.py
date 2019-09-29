from unittest import TestCase

from GeneradorEstadisticas import GeneradorEstadisticas


class TestGeneradorEstadisticas(TestCase):

    def test_calcular_estadisticas_cadena_vacia(self):
        self.assertEqual(GeneradorEstadisticas().calcular(""), [0], "estadisticas con cadena vacia")

    def test_calcular_estadisticas_con_un_numero(self):
        self.assertEqual(GeneradorEstadisticas().calcular("7"), [1,7,7,7], "estadisticas con un numero")

    def test_calcular_estadisticas_con_dos_numeros(self):
        self.assertEqual(GeneradorEstadisticas().calcular("7,3"), [2,3,7,5.0], "estadisticas con dos numeros")

    def test_calcular_estadisticas_con_n_numeros(self):
        self.assertEqual(GeneradorEstadisticas().calcular("7,3,0,4,6"), [5,0,7,4.0], "estadisticas con n numeros")