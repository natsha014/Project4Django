from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        """Метод для обработки POST-запроса (отправка формы)"""
        print(f"--- Тип запроса: {request.method} ---")
        print(request.POST)

        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} получено.")
