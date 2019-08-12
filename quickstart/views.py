from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
	return render(request, "quickstart/index.html")


def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'quickstart/register.html', {'form': form })
