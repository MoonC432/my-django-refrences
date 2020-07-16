from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .models import Course,Order
def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses':courses})

def pay(request, pk):
    client_id = settings.PAYPAL_CLIENT_ID
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'pay.html', {'course':course, 'client_id':client_id })
def create(request):
    print("here im")
    data = {}
    return JsonResponse(data)

def capture(request):
    data= {}
    return JsonResponse(data)

def getClientId(request):
    if request.method == "GET":        
        return JsonResponse({'client_id':  settings.PAYPAL_CLIENT_ID})