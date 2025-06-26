from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PictureForm, TextInputForm
from django.urls import reverse
from .project import gptout

# Create your views here.


def picture_view(request):

	if request.method == 'POST':
		form = PictureForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('submit_text')
	else:
		form = PictureForm()
	return render(request, 'picture_form.html', {'form': form})
	
def submit_text(request):
   if request.method == 'POST':
       form = TextInputForm(request.POST)
       if form.is_valid():
           global text_input; 
           text_input = form.cleaned_data['text_input']
           # Process the text_input string here
           return redirect('success')
   else:
       form = TextInputForm()
   return render(request, 'text_form.html', {'form': form})
	
def success(request):
    txt = request.POST['text_input']
    # print(txt)
    #return HttpResponse("expecting field")
    x = gptout(txt)
    return HttpResponse(x)


