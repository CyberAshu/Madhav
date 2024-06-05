from django.shortcuts import render, get_object_or_404
from .forms import EnrollForm
from .models import ResultImage
from django.http import HttpResponse

def home_view(request):
    error_message = None
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            roll_number = form.cleaned_data.get('roll_number')
            try:
                result_image = ResultImage.objects.get(roll_number=roll_number)
                return render(request, 'madhavapp/result.html', {'result_image': result_image})
            except ResultImage.DoesNotExist:
                error_message = 'No result found for the given roll number.'
    else:
        form = EnrollForm()
    return render(request, 'madhavapp/home.html', {'form': form, 'error_message': error_message})

def home(request):
    return render(request, 'home.html')