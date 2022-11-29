from django.shortcuts import render

from django.http import JsonResponse

def quick_home(request):
    sit = "violet evergarden"
    return render(request, 'crystal/base.html', {})

def css1(request):
    return render(request, 'crystal/css1.html', {})