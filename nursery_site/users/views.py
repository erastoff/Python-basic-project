from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

from users.forms import RegistrationForm, UserAuthenticationForm


class RegistrationView(CreateView):
    model = User
    # fields = ('username', 'email', 'password')
    form_class = RegistrationForm
    success_url = reverse_lazy("parents:index")
    template_name = "users/user_form.html"


class UserLoginView(LoginView):
    template_name = "users/login_form.html"
    form_class = UserAuthenticationForm
    # success_url = 'parents/'


class UserLogoutView(LogoutView):
    pass
    # template_name = 'users/login_form.html'
    # success_url = 'parents/'


# class UserDetailView(DetailView):
#     model = User
#     template_name = 'users/user_detail.html'
#
#     def get_queryset(self):
#         return super().get_queryset().filter(id=self.request.user.id)


# Позволяется не отображать PK на ссылке, в отличие от предыдущей вью
class UserTemplateView(TemplateView):
    template_name = "users/user_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.request.user
        return context
