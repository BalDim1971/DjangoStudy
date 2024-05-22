from django.contrib import admin, messages
from women.models import Women


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'
    
    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat',
                    'brief_info')
    list_display_links = ('id', 'title')
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', 'cat')
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']

    @admin.display(description='Краткое описание')
    def brief_info(self, women: Women) -> str:
        return f"Описание {len(women.content)} символов"

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset) -> None:
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записи(ей) сняты с публикации!",
                          messages.WARNING)
