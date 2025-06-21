from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UsernameField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]


class CustomUserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        required=True,
    )
    password2 = forms.CharField(
        label=_("Confirm new password"),
        widget=forms.PasswordInput,
        required=True,
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]
        field_classes = {"username": UsernameField}

    def clean_username(self):
        username = self.cleaned_data["username"]
        user_qs = User.objects.filter(username=username).exclude(pk=self.instance.pk)
        if user_qs.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password1 != password2:
            self.add_error("password2", _("Passwords do not match"))
        validate_password(password1, self.instance)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
