from django.test import LiveServerTestCase, Client

class LiveServerTests(LiveServerTestCase):

    def test_server_running(self):
        client = Client()
        response = client.get("/")
        self.assertIn(response.status_code, [200, 404])
