from django.shortcuts import render, render_to_response
from glia.models import Display

import random
# Create your views here.
def index(request):
    #rand = random.randint(0,3)
    #display = Display.objects.get(num=rand)
    return render_to_response('index.html', locals())
