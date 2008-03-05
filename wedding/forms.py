from django.newforms import ModelForm
from mysite.wedding.models import Comments

#CommentForm = form_for_model(Comments)
class CommentForm(ModelForm):
    class Meta:
        model = Comments
