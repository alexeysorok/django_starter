from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def bio(request, username):
    print(username)
    return render(request, "index.html")


def special_case_2003(request):
    print(request)
    return HttpResponse('special_case_2003')


def year_archive(request, year):
    print(request)
    print(type(request))
    print(year)
    print(type(year))
    return HttpResponse(year)


