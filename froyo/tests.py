from django.test import TestCase

# Create your tests here.
class IngredientsListPageTest(TestCase):
	
	def test_ingredients_list_page_returns_correct_html(self):
		response = self.client.get('/ingredients_list')
		self.assertTemplateUsed(response, 'ingredients_list.html')


class IngredientsDetailPageTest(TestCase):
	
	def test_ingredients_detail_page_returns_correct_html(self):
		response = self.client.get('/ingredients_detail')
		self.assertTemplateUsed(response, 'ingredients_detail.html')


class IngredientsUpdatePageTest(TestCase):
	
	def test_ingredients_update_page_returns_correct_html(self):
		response = self.client.get('/ingredients_update')
		self.assertTemplateUsed(response, 'ingredients_update_form.html')


class IngredientsCreatePageTest(TestCase):
	
	def test_ingredients_create_page_returns_correct_html(self):
		response = self.client.get('/ingredients_create')
		self.assertTemplateUsed(response, 'ingredients_create_form.html')


class RecipesListPageTest(TestCase):
	
	def test_recipes_list_page_returns_correct_html(self):
		response = self.client.get('/recipes_list')
		self.assertTemplateUsed(response, 'recipes_list.html')


class RecipesDetailPageTest(TestCase):
	
	def test_recipes_detail_page_returns_correct_html(self):
		response = self.client.get('/recipes_detail')
		self.assertTemplateUsed(response, 'recipes_detail.html')


class RecipesUpdatePageTest(TestCase):
	
	def test_recipes_update_page_returns_correct_html(self):
		response = self.client.get('/recipes_update')
		self.assertTemplateUsed(response, 'recipes_update_form.html')


class RecipesCreatePageTest(TestCase):
	
	def test_recipes_create_page_returns_correct_html(self):
		response = self.client.get('/recipes_create')
		self.assertTemplateUsed(response, 'recipes_create_form.html')


class OrdersListPageTest(TestCase):
	
	def test_orders_list_page_returns_correct_html(self):
		response = self.client.get('/orders_list')
		self.assertTemplateUsed(response, 'orders_list.html')


class OrdersDetailPageTest(TestCase):
	
	def test_orders_detail_page_returns_correct_html(self):
		response = self.client.get('/orders_detail')
		self.assertTemplateUsed(response, 'orders_detail.html')


class OrdersUpdatePageTest(TestCase):
	
	def test_orders_update_page_returns_correct_html(self):
		response = self.client.get('/orders_update')
		self.assertTemplateUsed(response, 'orders_update_form.html')


class OrdersCreatePageTest(TestCase):
	
	def test_ingredients_create_page_returns_correct_html(self):
		response = self.client.get('/orders_create')
		self.assertTemplateUsed(response, 'orders_create_form.html')