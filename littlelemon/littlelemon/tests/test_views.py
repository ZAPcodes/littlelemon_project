from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from restaurant.models import MenuItem, BookingTable
from restaurant.serializers import MenuSerializer, BookingTableSerializer
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

class MenuItemViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.menu_item = MenuItem.objects.create(title="Pizza", price=9.99, inventory=True)
        self.url = reverse('menuitem-list')

    def test_get_menu_items(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        menu_items = MenuItem.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.client.logout()

    def test_create_menu_item(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Burger',
            'price': 5.99,
            'inventory': True
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

class SingleMenuItemViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.menu_item = MenuItem.objects.create(title="Pizza", price=9.99, inventory=True)
        self.url = reverse('menuitem-detail', kwargs={'pk': self.menu_item.pk})

    def test_get_single_menu_item(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        menu_item = MenuItem.objects.get(pk=self.menu_item.pk)
        serializer = MenuSerializer(menu_item)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.client.logout()

    

class BookingViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.booking = BookingTable.objects.create(name="John Doe", no_of_guests=4, booking_date="2023-07-12T14:00:00Z")
        self.url = reverse('bookingtable-list')

    def test_get_bookings(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.url)
        bookings = BookingTable.objects.all()
        serializer = BookingTableSerializer(bookings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        self.client.logout()

    def test_create_booking(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'name': 'Jane Doe',
            'no_of_guests': 2,
            'booking_date': '2023-07-13T18:00:00Z'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()

    