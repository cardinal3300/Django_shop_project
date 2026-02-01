from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class FeedbackForm(forms.Form):
    """Форма обратной связи для страницы контактов.
    Позволяет пользователю отправить сообщение администрации сайта.
    Поля:
    - name: имя отправителя;
    - email: адрес электронной почты для обратного ответа;
    - message: текст сообщения."""

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
    """Форма создания и редактирования продукта с Bootstrap-стилизацией и валидацией."""

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "image",
            "category",
            "purchase_price",
            "status",
        ]

    def __init__(self, *args, **kwargs):
        """Добавляем классы Bootstrap для всех полей формы."""
        super(ProductForm, self).__init__(*args, **kwargs)

        # общая стилизация для текстовых и числовых полей
        for field_name, field in self.fields.items():
            if isinstance(
                field.widget,
                (forms.TextInput, forms.NumberInput, forms.Textarea, forms.Select),
            ):
                field.widget.attrs.update(
                    {
                        "class": "form-control",
                    }
                )
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update(
                    {
                        "class": "form-check-input",
                    }
                )
            elif isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs.update(
                    {
                        "class": "form-control",
                    }
                )

        # Дополнительные placeholder'ы для удобства
        self.fields["name"].widget.attrs["placeholder"] = "Введите название товара"
        self.fields["description"].widget.attrs[
            "placeholder"
        ] = "Введите описание товара"
        self.fields["purchase_price"].widget.attrs["placeholder"] = "Введите цену"
        self.fields["status"].widget.attrs["placeholder"] = "Статус публикации"

    def clean_name(self):
        """Проверка имени на запрещённые слова."""
        name = self.cleaned_data.get("name", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise ValidationError(
                    f"Название не может содержать запрещённое слово: «{word}»."
                )
        return name

    def clean_description(self):
        """Проверка описания на запрещённые слова."""
        description = self.cleaned_data.get("description", "")
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise ValidationError(
                    f"Описание не может содержать запрещённое слово: «{word}»."
                )
        return description

    def clean_purchase_price(self):
        """Проверка, что цена не отрицательная."""
        price = self.cleaned_data.get("purchase_price")
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
