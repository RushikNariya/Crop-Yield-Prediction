from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pickle

# Load the model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
# with open('sc.pkl', 'rb') as model_file:
#     sc = pickle.load(model_file)

def index(request):
    return render(request, "index.html")

# def home(request):
#     return render(request, "home.html")

def predict(request):
    if request.method == 'POST':
        N = int(request.POST.get('nitrogen'))
        P = int(request.POST.get('phosphorus'))
        K = int(request.POST.get('potassium'))
        temp = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))
        ph = float(request.POST.get('ph'))
        rainfall = float(request.POST.get('rainfall'))

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        prediction = model.predict(single_pred)

        crop_dict = {
            1: 'rice', 2: 'maize', 3: 'jute', 4: 'cotton', 5: 'coconut', 6: 'papaya', 7: 'orange', 8: 'apple',
            9: 'muskmelon', 10: 'watermelon', 11: 'grapes', 12: 'mango', 13: 'banana', 14: 'pomegranate', 15: 'lentil',
            16: 'blackgram', 17: 'mungbean', 18: 'mothbeans', 19: 'pigeonpeas', 20: 'kidneybeans', 21: 'chickpea', 22: 'coffee'
        }

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = "{} is the best crop to be cultivated".format(crop)
        else:
            result = "Sorry, we are not able to recommend a crop."

        return render(request, 'index.html', {'result': result})

                                                                                                                                  