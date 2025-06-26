# forms.py
from django import forms
from .models import Picture
from django.conf import settings



class PictureForm(forms.ModelForm):
	class Meta:
		model = Picture
		fields = ['Main_Input_Img']
		widgets = {'Main_Input_Img': forms.FileInput(attrs={'accept': 'image/*', 'capture':'camera'})}

class TextInputForm(forms.Form):
   text_input = forms.CharField(max_length=1000)
