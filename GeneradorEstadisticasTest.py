from unittest import TestCase

from GeneradorEstadisticas import GeneradorEstadisticas


class TestGeneradorEstadisticas(TestCase):

    def test_calcular_minimo_maximo_elementos_cadena_vacia(self):
        self.assertEqual(GeneradorEstadisticas().calcular(""), [0], "maximo con cadena vacia")

  #  def test_calcular_maximo_con_un_numero(self):
  #      self.assertEqual(GeneradorEstadisticas().calcular("3"), [1,3,3], "maximo con cadena un numero")

  #  def test_calcular_maximo_con_dos_numeros(self):
  #      self.assertEqual(GeneradorEstadisticas().calcular("3,10"), [2,3,10], "maximo con cadena dos numeros")

  #  def test_calcular_maximo_con_n_numeros(self):
  #      self.assertEqual(GeneradorEstadisticas().calcular("3,10,8,1,50"), [5,1,50], "maximo con cadena n numeros")

    def test_calcular_promedio_con_cadena_vacia(self):
        self.assertEqual(GeneradorEstadisticas().calcular(""), [0], "promedio con cadena vacia")

    def test_calcular_promedio_con_un_numero(self):
        self.assertEqual(GeneradorEstadisticas().calcular("7"), [1,7,7,7], "promedio con un numero")

