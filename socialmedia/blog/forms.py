from django import forms
from .models import Comment
from django.forms import Textarea

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('Comment',)
        widgets = {
            'Comment': Textarea(attrs={'cols': 30, 'rows': 2}),
   }
