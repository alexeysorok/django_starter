import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm


# Create your views here.
# def my_form(request):
#     return HttpResponse(MyForm().as_p())

# def my_form(request):
#     print(request.GET)
#     form = MyForm(request.GET or None)
#     if form.is_valid():
#         print("Valid")
#         print(form.cleaned_data)
#         print(form.errors)
#     else:
#         print("Not Valid")
#         print(form.errors)
#
#     return render(request, 'form_page.html', context={'form': form})

def my_form(request):
    print(request.FILES)
    form = MyForm(request.GET or None, request.FILES or None)

    if form.is_valid():
        print("Valid")
        print(form.cleaned_data)
        file_path = os.path.join(settings.MEDIA_ROOT,
                                 form.cleaned_data['profile_picture'].name)
        with open(file_path, 'wb+') as local_file:
            for chunk in form.cleaned_data['prosile_picture']:
                local_file.write(chunk)
    else:
        print("Not Valid")
        print(form.errors)

    return render(request, 'form_page.html', context={'form': form})

