from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Отображение блога в админке"""

    list_display = ("title", "is_published", "created_at", "views")
    list_filter = ("is_published",)
    search_fields = ("title", "content")
