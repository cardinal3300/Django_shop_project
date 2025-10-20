from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавляет тестовые категории и продукты в базу данных"

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING("Все старые данные удалены."))

        # Создаём категории
        electronics = Category.objects.create(name="Электроника", description="Гаджеты и техника")
        clothes = Category.objects.create(name="Одежда", description="Мужская и женская одежда")
        books = Category.objects.create(name="Книги", description="Художественная и научная литература")

        # Создаём продукты
        Product.objects.create(
            name="Смартфон Samsung Galaxy",
            description="Мощный телефон с большим экраном",
            purchase_price=899.99,
            category=electronics
        )

        Product.objects.create(
            name="Футболка Nike",
            description="Хлопковая футболка для повседневной носки",
            purchase_price=29.99,
            category=clothes
        )

        Product.objects.create(
            name="Книга '1984'",
            description="Классика антиутопии от Джорджа Оруэлла",
            purchase_price=14.50,
            category=books
        )

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно созданы!"))
