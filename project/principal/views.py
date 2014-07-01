from principal.models import Bebida , Receta , Comentario
from django.contrib.auth.models import User
from django.shortcuts import render_to_response , get_object_or_404
from django.http import HttpResponse, Http404


def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	return render_to_response('lista_bebidas.html',{'lista':bebidas})

def sobre(request):
	html = "<html><body>Proyecto akakkaka en MDW</body></hmtl>"
	return HttpResponse(html)
def inicio(request):
	recetas = Receta.objects.all()
	return render_to_response('inicio.html',{'recetas':recetas})
	pass
	
