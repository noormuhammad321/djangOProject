# object_detection/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from roboflow import Roboflow
rf = Roboflow(api_key="iIVsuHQBQwO0DiE3bE1K")
project = rf.workspace().project("boxandbarcode")
model = project.version(13).model



# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
from .forms import YourModelForm
from .models import YourModel
def home(request):
    return render(request, 'home.html')

import requests
def object_detection(request):
    if request.method == 'POST':
        form = YourModelForm(request.POST, request.FILES)
        if form.is_valid():
            image=form.save()
            model.predict(image.image.path, confidence=40, overlap=30).save(image.image.path)
            res=model.predict(image.image.path, confidence=40, overlap=30).json()
            print("HELLPOOO")
            os.system("cd")
            url=""
            requests.post(url, data = res)
            return render(request,"object_detection.html",{"Image":image,"response":res})  # Redirect to a success page
    else:
        form = YourModelForm()

    return render(request, 'object_detection.html', {'form': form})
    
    

def fine_tune_model(request):
    # Implement model fine-tuning logic here
    if request.method == 'POST':
        key_required=request.POST.get('api_key')
        print(key_required)
    return render(request, 'fine_tune_model.html', {'message': ""})
