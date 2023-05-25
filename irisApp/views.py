from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    if request.method == 'POST':
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']
        # sl = request.POST.get('sepal_length')
        # sw = request.POST.get('sepal_width')
        # pl = request.POST.get('petal_length')
        # pw = request.POST.get('petal_width')
        # contact = flower(sepal_length=sl, sepal_width=sw, petal_length=pl, petal_width=pw)
        # contact.save()
        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        if y_pred[0] == 0:
            y_pred = 'Setosa'
        elif y_pred[0] == 1:
            y_pred = 'Verscicolor'
        else:
            y_pred = 'Virginica'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')
