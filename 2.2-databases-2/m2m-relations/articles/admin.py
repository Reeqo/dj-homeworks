from django.contrib import admin
from .models import Article, ArticleSection, Section
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        has_selected_sections = False
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                continue
            if form.cleaned_data.get('is_main'):
                has_selected_sections = True
                break
        if not has_selected_sections:
            raise ValidationError('Укажите основной раздел')
        main_section_count = 0
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                continue
            if form.cleaned_data.get('is_main'):
                main_section_count += 1
        if main_section_count == 0:
            raise ValidationError('Укажите основной раздел!')
        elif main_section_count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    formset = ArticleSectionInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [ArticleSectionInline]



@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']
