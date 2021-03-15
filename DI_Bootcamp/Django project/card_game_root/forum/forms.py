from django import forms
from .models import *
from django.contrib.auth.models import User

class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = [
            'title',
            'comment',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment',
        ]