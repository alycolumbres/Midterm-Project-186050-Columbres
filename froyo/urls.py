from django.conf.urls import url

from .views import IngredientsListView, IngredientsDetailView, IngredientsUpdateView, IngredientsCreateView, RecipesListView, RecipesDetailView, RecipesUpdateView, RecipesCreateView, OrdersListView, OrdersDetailView, OrdersUpdateView, OrdersCreateView


urlpatterns = [
	url(r'^ingredients_list$', IngredientsListView.as_view(), name='Ingredients_List_View'),
	url(r'^ingredients_detail$', IngredientsDetailView.as_view(), name='Ingredients_Detail_View'),
	url(r'^ingredients_update$', IngredientsUpdateView.as_view(), name='Ingredients_Update_View'),
	url(r'^ingredients_create$', IngredientsCreateView.as_view(), name='Ingredients_Create_View'),

	url(r'^recipes_list$', RecipesListView.as_view(), name='Recipes_List_View'),
	url(r'^recipes_detail$', RecipesDetailView.as_view(), name='Recipes_Detail_View'),
	url(r'^recipes_update$', RecipesUpdateView.as_view(), name='Recipes_Update_View'),
	url(r'^recipes_create$', RecipesCreateView.as_view(), name='Recipes_Create_View'),

	url(r'^orders_list$', OrdersListView.as_view(), name='Orders_List_View'),
	url(r'^orders_detail$', OrdersDetailView.as_view(), name='Orders_Detail_View'),
	url(r'^orders_update$', OrdersUpdateView.as_view(), name='Orders_Update_View'),
	url(r'^orders_create$', OrdersCreateView.as_view(), name='Orders_Create_View'),
]