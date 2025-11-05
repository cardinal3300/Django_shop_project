from django import forms
from django.core.exceptions import ValidationError

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
        fields = "__all__"  # показываем все поля модели

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # всем полям добавляем одинаковый стиль Bootstrap
            field.widget.attrs["class"] = "form-control"
        # отдельно стилизуем булевое поле (чекбокс)
        if "is_published" in self.fields:
            self.fields["is_published"].widget.attrs["class"] = "form-check-input"

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image
        # Проверка формата
        if image.content_type not in ALLOWED_IMAGE_TYPES:
            raise ValidationError("Допустимы только изображения JPEG или PNG.")
        # Проверка размера
        if image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
            raise ValidationError(
                f"Размер файла не должен превышать {MAX_IMAGE_SIZE_MB} МБ."
            )
        return image

    def clean_name(self):
        """Проверка имени на запрещённые слова."""
        name = self.cleaned_data.get("name", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise forms.ValidationError(
                    f"Название не должно содержать запрещённое слово: '{word}'"
                )
        return name

    def clean_description(self):
        """Проверка описания на запрещённые слова."""
        description = self.cleaned_data.get("description", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise forms.ValidationError(
                    f"Описание не должно содержать запрещённое слово: {word}"
                )
        return description

    def clean_purchase_price(self):
        """Проверка, что цена не отрицательная."""
        price = self.cleaned_data.get("purchase_price")
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
