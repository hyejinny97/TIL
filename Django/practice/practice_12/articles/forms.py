from socket import fromshare
from django import forms
from .models import Article
from django.utils.translation import gettext_lazy as _

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': _('제목'),
            'content': _('내용'),
            'image': _('이미지 파일 첨부'),
            'thumbnail': _('썸네일 이미지 파일 첨부'),
        }