from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from .views import SlotView


class TestSlot(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SlotView.as_view({'get': 'list'})
        self.uri1 = '/slots/'
        self.uri2 = '/schedule/?interviewer=1&candidate=1'

    def test_slots(self):
        request = self.factory.get(self.uri1)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
    
    def test_schedule(self):
        request = self.factory.get(self.uri2)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
