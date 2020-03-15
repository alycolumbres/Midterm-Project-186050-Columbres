from django.views.generic import ListView, DetailView, UpdateView, CreateView

# Create your views here.
class IngredientsListView(ListView):
	template_name = 'ingredients_list.html'


class IngredientsDetailView(DetailView):
	template_name = 'ingredients_detail.html'


class IngredientsUpdateView(UpdateView):
	template_name = 'ingredients_update_form.html'


class IngredientsCreateView(CreateView):
	template_name = 'ingredients_create_form.html'


class RecipesListView(ListView):
	template_name = 'recipes_list.html'


class RecipesDetailView(DetailView):
	template_name = 'recipes_detail.html'


class RecipesUpdateView(UpdateView):
	template_name = 'recipes_update_form.html'


class RecipesCreateView(CreateView):
	template_name = 'recipes_create_form.html'


class OrdersListView(ListView):
	template_name = 'orders_list.html'


class OrdersDetailView(DetailView):
	template_name = 'orders_detail.html'


class OrdersUpdateView(UpdateView):
	template_name = 'orders_update_form.html'


class OrdersCreateView(CreateView):
	template_name = 'orders_create_form.html'