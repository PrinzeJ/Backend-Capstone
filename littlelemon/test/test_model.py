from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(name="IceCream", price=80, description="Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima quod sequi asperiores, laboriosam repellat ipsam temporibus? Vero adipisci consequatur architecto, dolore labore maxime necessitatibus voluptatem consectetur nobis expedita nihil dicta.")
    self.assertEqual(str(item), "IceCream:80")