from django.db import models
from django.urls import reverse


class PublishedModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_published=Women.Status.PUBLISHED
        )


class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            verbose_name='URL')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices,
                                       default=Status.DRAFT)
    cat = models.ForeignKey('cats.Category',
                            on_delete=models.PROTECT,
                            related_name='posts')
    
    objects = models.Manager()
    published = PublishedModel()

    class Meta:
        """
        Сортировка статей по времени создания.
        Поде сделано индексируемым для более быстрой сортировки.
        """
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create']),
        ]
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title
