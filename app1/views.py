from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse('this is string as a response')

def html(request):
    return render(request, 'app1.html')
