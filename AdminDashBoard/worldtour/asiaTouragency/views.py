from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def index(request):
#     return HttpResponse("ASIA TOUR AGENCY")
from .models import Tour
def index(request):
    tours=Tour.objects.all()
    context={'tours':tours}
    return render(request, 'tours/index.html',context)