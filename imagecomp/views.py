# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import numpy as np
import cv2

# Create your views here.

#Class here just for testing laziness
class ImageForm(forms.Form):

    pic1 = forms.ImageField()
    pic2 = forms.ImageField()


#image uploader
def image(request):

    if request.method == 'POST':
        MyImageForm = ImageForm(request.POST, request.FILES)
        
        #Reading the files directly, not yet sure why cleaned_data doesnt work
        if MyImageForm.is_valid():
            pic1_lnk = request.FILES['pic1']
            pic2_lnk = request.FILES['pic2'] 
            

            #I had to turn the images to numpy then cv so I could get 3d array
            pic1 = cv2.imdecode(np.fromstring(pic1_lnk.read(),np.uint8), cv2.CV_LOAD_IMAGE_UNCHANGED)
            pic2 = cv2.imdecode(np.fromstring(pic2_lnk.read(),np.uint8), cv2.CV_LOAD_IMAGE_UNCHANGED)
            pic1 = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)
            pic2 = cv2.cvtColor(pic2, cv2.COLOR_BGR2GRAY)
            

            #Calculations for errors between two imaeges
            err = np.sum((pic1.astype("float") - pic2.astype("float")) ** 2)
	    err /= float(pic1.shape[0] * pic2.shape[1])
            

            if err < 2000:
                text = 'images are the similar!'
                return HttpResponse(text)
            else:
                text = 'images are the different!'
                return HttpResponse(text)
        else:
            MyImageForm = ImageForm()

    return render(request,'upload.html',locals())
