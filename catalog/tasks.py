from celery import shared_task

from catalog.models import Product


@shared_task
def check_products(pk, model):
    pass

