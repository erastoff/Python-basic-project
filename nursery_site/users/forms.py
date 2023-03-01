from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Widget


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(help_text="")
    password1 = forms.CharField(
        help_text="", widget=forms.PasswordInput(), label="Password"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"


class UserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    username = forms.CharField(help_text="")
    # password1 = forms.CharField(help_text='', widget=forms.PasswordInput(), label='Password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
