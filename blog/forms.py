from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """Форма для создания и редактирования блогов с Bootstrap-стилизацией."""

    class Meta:
        model = BlogPost
        fields = ["title", "content", "preview", "is_published"]

    def __init__(self, *args, **kwargs):
        """Добавляем классы Bootstrap для всех полей формы."""

        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите заголовок"
        })
        self.fields["content"].widget.attrs.update({
            "class": "form-control",
            "rows": 5,
            "placeholder": "Введите содержимое"
        })
        self.fields["preview"].widget.attrs.update({
            "class": "form-control",
        })
        self.fields["is_published"].widget.attrs.update({
            "class": "form-check-input",
        })
