from django.test import TestCase
from .models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=True)
        self.assertEqual(item.title, "IceCream")