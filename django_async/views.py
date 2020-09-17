from django.http import HttpResponse
from django.shortcuts import render
from .forms import my_form


# Create your views here.
def main(request):
    form = my_form()
    context = {'form': form,
               }
    template = 'django_async/main.html'
    if request.method == "POST":
        return HttpResponse('Form Submitted')

    return render(request, template, context=context)
