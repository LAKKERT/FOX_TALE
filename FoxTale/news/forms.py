from django import forms
from .models import NewsContent
from datetime import date

class NewsForm(forms.ModelForm):
    title = forms.CharField( max_length=35 ,widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'title',
        'placeholder': 'TITLE',
        'class': 'input_field',
    }))

    introduction_content = forms.CharField(max_length=158 ,widget=forms.Textarea(attrs={
        'class': 'introduction_textarea',
        'placeholder': 'Write an introductory content',
        'cols': '30',
        'rows': '10',
    }))

    cover = forms.FileField(widget=forms.FileInput(attrs={
        'type': 'file',
        'id': 'file-upload'
    }))

    Paragraph_title = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'name': 'Paragraph_title',
        'placeholder': 'PARAGRAPH TITLE',
        'class': 'Paragraph_title',
    }))

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'introduction_textarea',
        'placeholder': 'Write the content',
        'cols': '30',
        'rows': '10',  
    }))

    date_add = forms.DateField(initial=date.today)

    class Meta:
        model = NewsContent
        fields = ['introduction_content','title','cover', 'Paragraph_title', 'content', 'date_add']
