from django.shortcuts import render, redirect
from my_app.models import *
from my_app.forms import *

def index(request):
    weights = Weight.objects.all().order_by("-date")
    foods = Food.objects.all()
    if request.method == "POST":
        form = WeightForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = WeightForm()
    #return render_to_response('my_app/index.html', {'weights': weights, 'foods': foods, 'form':form},)
    return render(request, 'my_app/index.html', {'weights': weights, 'foods': foods, 'form':form},)
