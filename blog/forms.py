from django import forms
from .models import Post, Point


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'map_href')


class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ('post', 'title', 'sequence_number', 'text',)