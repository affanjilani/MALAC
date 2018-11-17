# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def getImage(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Do all the facial recognition here
            return HttpResponseRedirect('/success/url/') # Change this to send to mobile and maybe JSON form
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

# Create your views here.
