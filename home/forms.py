from django.forms.widgets import TextInput, EmailInput
from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import Contact
from django.forms import ModelForm
from django.contrib.auth.models import User

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'surname', 'email', 'message']


class ChangeProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),


        }



class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        label="Eski parol",
        widget=forms.PasswordInput(),
        strip=False,
    )
    new_password1 = forms.CharField(
        label="Yangi parol",
        widget=forms.PasswordInput(),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="Yangi parolni tasdiqlash",
        widget=forms.PasswordInput(),
        strip=False,
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        # Orbit/Bootstrap ko‘rinishi
        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "autocomplete": "off",
            })

        self.fields["old_password"].widget.attrs.update({"autocomplete": "current-password"})
        self.fields["new_password1"].widget.attrs.update({"autocomplete": "new-password"})
        self.fields["new_password2"].widget.attrs.update({"autocomplete": "new-password"})

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError("Eski parol noto‘g‘ri.")
        return old_password

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("new_password1")
        p2 = cleaned.get("new_password2")

        if p1 and p2 and p1 != p2:
            self.add_error("new_password2", "Yangi parollar mos kelmadi.")

        if p1:
            try:
                password_validation.validate_password(p1, self.user)
            except ValidationError as e:
                self.add_error("new_password1", e)

        return cleaned

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data["new_password1"])
        if commit:
            self.user.save(update_fields=["password"])
        return self.user







