from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

from .forms import UserRegisterForm, UserLoginForm, UserProfileForm
from .models import User


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        # отправка приветственного письма
        send_mail(
            subject="Добро пожаловать в Django_Shop!",
            message=f"Привет, {form.instance.email}! 🎉 Спасибо за регистрацию в нашем магазине.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.instance.email],
            fail_silently=True,
        )

        return response


class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = UserLoginForm

    def get_success_url(self):
        return reverse_lazy("users:login")


class UserLogoutView(LogoutView):
    template_name = "users/logout.html"


class UserProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        # пользователь может редактировать только свой профиль
        return self.request.user
    