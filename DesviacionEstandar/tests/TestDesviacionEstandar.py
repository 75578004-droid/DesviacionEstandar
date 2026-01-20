import unittest
from src.logica.DesviacionEstandar import DesviacionEstandar


class TestDesviacionEstandar(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        desviacion = DesviacionEstandar([])
        self.assertIsNone(desviacion.calcular())

    def test_unElemento_retornaCero(self):
        desviacion = DesviacionEstandar([5])
        self.assertEqual(0.0, desviacion.calcular())

    def test_dosElementos_retornaDesviacion(self):
        desviacion = DesviacionEstandar([2, 4])
        self.assertEqual(1.0, desviacion.calcular())

    def test_nElementosSinDispersion_retornaCero(self):
        desviacion = DesviacionEstandar([5, 5, 5, 5])
        self.assertEqual(0.0, desviacion.calcular())

    def test_nElementosConDispersion_retornaDesviacion(self):
        desviacion = DesviacionEstandar([2, 4, 6, 8])
        self.assertAlmostEqual(2.236, desviacion.calcular(), places=3)