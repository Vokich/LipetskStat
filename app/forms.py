from django import forms
from .models import Attractions, News

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attractions
        fields = ['title', 'picture', 'description']


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }
        labels = {
            'title': 'Заголовок новости',
            'content': 'Текст новости',
            'image': 'Изображение (необязательно)',
        }
