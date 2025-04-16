import unittest
from excepciones import ingrese_numero
from excepciones import NumeroDebeSerPositivo
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(
            'builtins.input',
            return_value = '100'
    )

    def test_ingreso_numero(self, patched_input):
        numer = ingrese_numero()
        self.assertEqual(numer, 100)
