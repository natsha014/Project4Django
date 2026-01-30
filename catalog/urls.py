from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/contacts/', ContactsTemplateView.as_view(), name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
