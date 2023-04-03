from django import forms
from .models import Post, Point


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ('title', 'text', 'map_href')


class PointForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PointForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Point
        fields = ('post', 'title', 'sequence_number', 'text', 'map_href',)
