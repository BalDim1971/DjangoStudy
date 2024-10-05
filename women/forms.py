from sqlite3.dbapi2 import paramstyle
from xml.dom import ValidationErr

from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from women.models import Husband, Women
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


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label='Категория',
                                 empty_label='Категория не выбрана')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(),
                                     required=False, label='Муж',
                                     empty_label='Не замужем')

    class Meta:
        model = Women
        fields = ['title',
                  'slug',
                  'content',
                  'is_published',
                  'cat',
                  'husband',
                  'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels = {'slug': 'URL'}
    
    # Вариант валидатора для применения внутри класса
    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError("Должны быть только русские символы, дефис и пробел.")
        if len(title) > 50:
            raise ValidationError("Название не должно превышать 50 символов.")

        return title
