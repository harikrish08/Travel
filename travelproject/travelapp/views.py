from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import place, team


def demo(request):
    obj = place.objects.all()
    obj1=team.objects.all()
    return render(request, 'index.html', {'result': obj,'result1':obj1})



