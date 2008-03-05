from mysite.wedding.models import Comments
from django.newforms import form_for_model

CommentForm = form_for_model(Comments)
