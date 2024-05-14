from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            verbose_name='URL')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    class Meta:
        """
        Сортировка статей по времени создания.
        Поде сделано индексируемым для более быстрой сортировки.
        """
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]
    
    def __str__(self):
        return self.title
