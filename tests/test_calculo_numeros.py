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

@patch(
            'builtins.input',
            return_value = '-100' #""inventa un valor falso que deberia ingresarse por el input""
    )
    
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo): # with mismo que exception y try, pero para los test
            ingrese_numero()
            ...

@patch(
            'builtins.input',
            return_value = 'aaa'
    )

    def test_ingreso_letra(self, patch_input):
        with self.assertRaises(ValueError): #assertRaises() to verify that a specific exception gets raised.
            ingrese_numero()


if __name__ == '__main__':
    unittest.main()