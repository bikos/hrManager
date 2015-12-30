from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return HttpResponse("Hello bald, you're into our apps")


def post_list(request):
    return render(request, 'index.html', {})

