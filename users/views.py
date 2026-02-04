from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.conf import settings
from .forms import UserRegisterForm
from .models import User
from django.core.mail import send_mail
from django.contrib.auth import login


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=True
        )
