from django import forms


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
