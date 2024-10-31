from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenuView(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=150, inventory=50)
        Menu.objects.create(title="Burger", price=120, inventory=75)

    def test_get_menu(self):
        menu = Menu.objects.get(title="IceCream")
        self.assertEqual(menu.title, "IceCream")
        self.assertEqual(menu.price, 80)
        self.assertEqual(menu.inventory, 100)

    def test_getall(self):
        menus = Menu.objects.all()
        serialized_menus = MenuSerializer(menus, many=True)
        expected_data = [
            {'id': menus[0].id, 'title': 'IceCream', 'price': '80.00', 'inventory': 100},
            {'id': menus[1].id, 'title': 'Pizza', 'price': '150.00', 'inventory': 50},
            {'id': menus[2].id, 'title': 'Burger', 'price': '120.00', 'inventory': 75},
        ]
        self.assertEqual(serialized_menus.data, expected_data)