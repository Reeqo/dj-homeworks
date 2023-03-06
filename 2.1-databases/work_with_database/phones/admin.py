from django.contrib import admin
from .models import Phone

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
