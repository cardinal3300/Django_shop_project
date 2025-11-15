from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 1. Создаём группу
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        # 2. Получаем content type для модели Product
        product_ct = ContentType.objects.get_for_model(Product)

        # 3. Добавляем права
        can_unpublish = Permission.objects.get(
            codename="can_unpublish_product", content_type=product_ct
        )

        group.permissions.add(can_unpublish)

        self.stdout.write(
            self.style.SUCCESS(
                f"✅ Группа 'Модератор продуктов' создана и получила нужные права"
            )
        )
