from django import forms
from .models import GuessNumbers

class PostForm(forms.models):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',)
