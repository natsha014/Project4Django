from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def has_permission(self):
        """Проверяем: ты либо владелец, либо модератор с правом"""
        product = self.get_object()
        user = self.request.user

        is_owner = product.owner == user
        is_moderator = user.has_perm('catalog.can_unpublish_product')

        return is_owner or is_moderator or user.is_superuser


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def has_permission(self):
        product = self.get_object()
        user = self.request.user

        is_owner = product.owner == user
        is_moderator = user.has_perm('catalog.delete_product')

        return is_owner or is_moderator or user.is_superuser


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        """Метод для обработки POST-запроса (отправка формы)"""
        print(f"--- Тип запроса: {request.method} ---")
        print(request.POST)

        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} получено.")
