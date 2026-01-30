from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from blog.models import Post
from django.conf import settings


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            self.send_congratulations_email()
        return self.object

    def send_congratulations_email(self):
        subject = 'Поздравляем с достижением!'
        message = f'Статья "{self.object.title}" набрала 100 просмотров! Я молодец!'
        send_email_to = 'your-email@example.com'

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [send_email_to],
            fail_silently=True,
        )


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'content', 'preview', 'is_published')  # Добавили признак публикации
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')


class PostTemplateView(TemplateView):
    template_name = 'blog/contacts.html'

    def post(self, request, *args, **kwargs):
        """Метод для обработки POST-запроса (отправка формы)"""
        print(f"--- Тип запроса: {request.method} ---")
        print(request.POST)

        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f"Спасибо, {name}! Ваше сообщение {message} получено.")
