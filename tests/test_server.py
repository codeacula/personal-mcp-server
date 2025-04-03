import unittest
from fastapi.testclient import TestClient
from src.server.main import app  # Assuming 'app' is the FastAPI app instance

class TestServer(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_api_endpoint(self):
        response = self.client.post("/api", json={"type": "greet", "body": {"name": "Test"}})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello, Test!"})

    def test_data_endpoint(self):
        response = self.client.post("/data", json={"data": {"key": "value"}})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'success', 'data': {'key': 'value'}})

    def test_error_handling(self):
        response = self.client.post("/api", json={"type": "unknown"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'Unknown request type.'})

if __name__ == '__main__':
    unittest.main()