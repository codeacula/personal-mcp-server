import unittest
from src.server.main import app  # Assuming 'app' is the Flask/FastAPI app instance

class TestServer(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the MCP Server', response.data)  # Adjust based on actual response content

    def test_some_endpoint(self):
        response = self.client.get('/some-endpoint')  # Replace with actual endpoint
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on expected response

if __name__ == '__main__':
    unittest.main()