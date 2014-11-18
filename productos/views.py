from django.shortcuts import render
from productos.models import Categoria, Imagenes
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.
def inicio(request):
    imagenes = Imagenes.objects.all()
    return render_to_response('index.html',{'imagenes':imagenes})

