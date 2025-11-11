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


# Список запрещённых слов
FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]

# Максимальное значение рисунка и возможный список форматов
MAX_IMAGE_SIZE_MB = 5
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png"]


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования продукта с валидацией."""

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "purchase_price"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "purchase_price": forms.NumberInput(attrs={"step": 0.01}),
        }
