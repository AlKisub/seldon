from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'date':
                visible.field.widget.input_type = 'datetime-local'
                visible.field.widget.attrs['style'] = 'width:250px'
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = News
        fields = ('subject', 'text', 'date')
