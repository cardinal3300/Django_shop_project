from django.shortcuts import render
from .forms import FeedbackForm


def home(request):
    """
    Контроллер для отображения домашней страницы.
    Возвращает шаблон home.html.
    """
    return render(request, 'catalog/home.html')

def contacts(request):
    """
    Контроллер для отображения страницы с контактной информацией.
    """
    success_message = None  # сообщение об успешной отправке
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # здесь можно добавить логику отправки email или сохранения данных в БД
            success_message = "Спасибо! Ваше сообщение успешно отправлено."
            form = FeedbackForm()  # очистим форму после успешной отправки
    else:
        form = FeedbackForm()

    context = {
        'form': form,
        'success_message': success_message,
    }
    return render(request, 'catalog/contacts.html', context)