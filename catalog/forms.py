from django import forms

from .models import Product


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите имя"}
        ),
    )
    email = forms.EmailField(
        label="Ваш email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введите email"}
        ),
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Ваше сообщение...",
            }
        ),
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "purchase_price"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "purchase_price": forms.NumberInput(attrs={"step": 0.01}),
        }
