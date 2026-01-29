from blog.apps import BlogConfig
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostTemplateView

app_name = BlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/create/', PostCreateView.as_view(), name='post_create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('blog/contacts/', PostTemplateView.as_view(), name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
