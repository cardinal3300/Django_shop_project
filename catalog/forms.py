from django import forms
from django.core.exceptions import ValidationError
from .models import Product


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Ваше имя",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )
    email = forms.EmailField(
        label="Ваш email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ваше сообщение...'})
    )

# Список запрещённых слов (игнорируем регистр)
FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования продукта с валидацией."""
    class Meta:
        model = Product
        fields = '__all__' # показываем все поля модели
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        """Проверка имени на запрещённые слова."""
        name = self.cleaned_data.get('name', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower():
                raise forms.ValidationError(f"Название не должно содержать запрещённое слово: '{word}'")
        return name

    def clean_description(self):
        """Проверка описания на запрещённые слова."""
        description = self.cleaned_data.get('description', '')
        for word in FORBIDDEN_WORDS:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Описание не должно содержать запрещённое слово: {word}")
        return description

    def clean_purchase_price(self):
        """Проверка, что цена не отрицательная."""
        price = self.cleaned_data.get('purchase_price')
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price
