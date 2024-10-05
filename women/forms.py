from sqlite3.dbapi2 import paramstyle
from xml.dom import ValidationErr

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from women.models import Husband
from cats.models import Category


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- '
    code = 'russian'
    
    def __init__(self, message=None):
        self.message = message \
            if message \
            else 'Должны присутствовать только русские символы, дефис и пробел.'
    
    def __call__(self, value):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationErr(self.message,
                                code=self.code,
                                params={'value': value})


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255, min_length=5, label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        validators=[RussianValidator(),],
        error_messages={
            'min_length': 'Заголовок должен быть больше 5 символов',
            'required': 'Заголовок обязательно для заполнения',
        }
    )
    slug = forms.SlugField(
        max_length=255, label='Ссылка',
        validators=[
            MinLengthValidator(5, message='Минимум 5 символов'),
            MaxLengthValidator(100, message='Максимум 100 символов'),
        ])
    content = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        required=False, label='Контекст'
    )
    is_published = forms.BooleanField(required=False,
                                      label='Статус',
                                      initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label='Категория',
                                 empty_label='Категория не выбрана')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),
                                     required=False, label='Муж',
                                     empty_label='Не замужем')
    
    # Вариант валидатора для применения внутри класса
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    #     if not (set(title) <= set(ALLOWED_CHARS)):
    #         raise ValidationError("Должны быть только русские символы, дефис и пробел.")
    #
    #     return title
