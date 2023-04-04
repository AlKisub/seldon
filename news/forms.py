from django import forms
from .models import News


class NewsForm(forms.ModelForm):
    date = forms.DateField(label='Дата рождения', widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}), required=False)
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = News
        fields = ('subject', 'text', 'date')
