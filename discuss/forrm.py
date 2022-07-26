from django import forms

from .models import Comments


class add_comment(forms.ModelForm):

   class Meta:
       model = Comments
       # fields = '__all__'
       fields = ( 'body',)
       widgets = {
           'body':forms.Textarea()
       }