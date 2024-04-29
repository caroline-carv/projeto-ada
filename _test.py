import unittest

from app import app, calc


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calc.soma(1, 2), 3)
        self.assertEqual(calc.soma(-1, 1), 0)
        self.assertEqual(calc.soma(0, 0), 0)


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Primeiro n\xc3\xbamero', response.data)
        self.assertIn(b'Segundo n\xc3\xbamero', response.data)
        self.assertIn(b'Calcular Soma', response.data)

    def test_home_route_post(self):
        response = self.app.post('/', data={'num1': 2, 'num2': 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'resultado': 5})


if __name__ == '__main__':
    unittest.main()
