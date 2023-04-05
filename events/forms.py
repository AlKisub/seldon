from django import forms
from .models import Events


class EventsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'date':
                visible.field.widget.input_type = 'datetime-local'
                visible.field.widget.attrs['style'] = 'width:250px'
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Events
        fields = ('subject', 'text', 'date')
