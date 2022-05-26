from dataclasses import fields
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user_name", "user_email", "comment"]
        labels = {
            "user_name": "Your name",
            "user_email": "Your email",
            "comment": "Your comment"
        }
