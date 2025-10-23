from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .titanic_model import TitanicModel
import json


def index(request):
    return render(request, 'minilang/index.html')

@csrf_exempt
def predict_survival(request):
    """
    API endpoint para predecir la supervivencia en el Titanic
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pclass = int(data.get('pclass', 3))  # 1, 2 o 3
            sex = data.get('sex', 'male')  # 'male' o 'female'
            age = float(data.get('age', 30))
            fare = float(data.get('fare', 20))
            
            model = TitanicModel()
            prediction = model.predict_survival(pclass, sex, age, fare)
            
            return JsonResponse({
                'success': True,
                'prediction': prediction
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
