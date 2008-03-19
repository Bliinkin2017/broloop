#from django.newforms import ModelForm
from django import newforms as forms
from mysite.wedding.models import Comments, RSVP

class DijitText(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs',{}).update({'dojoType': 'dijit.form.TextBox', 'trim': 'true'})
        super(DijitText, self).__init__(*args, **kwargs)

class DijitBoolean(forms.CheckboxInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs',{}).update({'dojoType': 'dijit.form.CheckBox'})
        super(DijitBoolean, self).__init__(*args, **kwargs)

class DijitTextArea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs',{}).update({'dojoType': 'dijit.form.Textarea'})
        super(DijitTextArea, self).__init__(*args, **kwargs)

class DijitNumberSpinner(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs',{}).update({'dojoType': 'dijit.form.NumberSpinner', 'value': '0', 'size': '6', 'constraints': '{min:0,max:100}'})
        super(DijitNumberSpinner, self).__init__(*args, **kwargs)

#class CommentForm(ModelForm):
#    class Meta:
#        model = Comments

class CommentForm(forms.Form):
    name = forms.CharField(widget=DijitText)
    content = forms.CharField(widget=DijitTextArea)

class RSVPForm(forms.Form):
    name = forms.CharField(widget=DijitText)
    will_attend = forms.BooleanField(widget=DijitBoolean, label="Will Attend?", required=False)
    num_guests = forms.IntegerField(widget=DijitNumberSpinner, required=False, label="Total Number of Guests")
    additional_guests = forms.CharField(widget=DijitTextArea, required=False, label="Additional Guest Names")
