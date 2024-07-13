from django.test import TestCase
from restaurant.models import BookingTable, MenuItem
from django.utils import timezone

class BookingTableModelTest(TestCase):

    def setUp(self):
        # Set up a BookingTable instance
        self.booking = BookingTable.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=timezone.now()
        )

    def test_booking_table_creation(self):
        # Test if the booking table instance is created correctly
        self.assertTrue(isinstance(self.booking, BookingTable))
        self.assertEqual(self.booking.__str__(), self.booking.name)

    def test_get_item(self):
        # Test the get_item method
        expected_string = f'{self.booking.name} : {str(self.booking.no_of_guests)}'
        self.assertEqual(self.booking.get_item(), expected_string)

class MenuItemModelTest(TestCase):

    def setUp(self):
        # Set up a MenuItem instance
        self.menu_item = MenuItem.objects.create(
            title="Pizza",
            price=9.99,
            inventory=True
        )

    def test_menu_item_creation(self):
        # Test if the menu item instance is created correctly
        self.assertTrue(isinstance(self.menu_item, MenuItem))
        self.assertEqual(self.menu_item.__str__(), self.menu_item.title)

    def test_menu_item_fields(self):
        # Test the fields of the menu item instance
        self.assertEqual(self.menu_item.title, "Pizza")
        self.assertEqual(self.menu_item.price, 9.99)
        self.assertTrue(self.menu_item.inventory)
