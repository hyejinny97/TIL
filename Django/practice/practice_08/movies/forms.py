from django import forms
from .models import Movie
from django.utils.translation import gettext_lazy as _

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            'title': _('영화 제목'),
            'summary': _('영화 줄거리'),
            'running_time': _('상영 시간'),
            'imgfile': _('파일 첨부'),
        }