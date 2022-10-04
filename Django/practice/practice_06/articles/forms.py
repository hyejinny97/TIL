from cProfile import label
from dataclasses import field
from tkinter.tix import Form
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 10}),
        }
        labels = {
            "title": "제목",
            "content": "내용",
        }
