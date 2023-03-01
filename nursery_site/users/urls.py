from django.urls import path

from .views import RegistrationView, UserLoginView, UserLogoutView, UserTemplateView

app_name = "users"

urlpatterns = [
    path("create/", RegistrationView.as_view(), name="registration"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    # path("account/<int:pk>/", UserDetailView.as_view(), name="account"),
    path("user-profile/", UserTemplateView.as_view(), name="user-profile"),
]
