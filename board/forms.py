from django import forms
from .models import Board
from django.contrib.auth.models import User


# 게시글 작성 폼
# 가져오는 값 : id, title, content
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content', 'author')
