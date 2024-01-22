from django import forms
from django.contrib.auth.models import User
from .models import SupportModel, MessageModel

class CreateRoom(forms.ModelForm):
    reason_title = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'reason_title',
        'placeholder': 'TITLE REASON',
        'class': 'support_chat_create_fields',
        'type': 'text',
        'id': 'id_reason_title',
    }))

    problem = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text',
        'placeholder': 'DISCRIPTION YOUR PROBLEM',
        'class': 'text_area_problem',
    }))

    class Meta:
        model = SupportModel
        fields = [
            'reason_title',
            'problem',
        ]

class SendMessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'type': 'text',
        'placeholder': 'Write something',
        'class': 'content_field',
    }))

    class Meta:
        model = MessageModel
        fields = [
            'content'
        ]