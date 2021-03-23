from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. ef13ab03 is the polls index.")