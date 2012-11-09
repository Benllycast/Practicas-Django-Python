# Create your views here.
from principal.models import Receta, Comentario
from principal.form import ContactoForm, RecetaForm, ComentarioForm
from django.shortcuts import render_to_response, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage



def listar_bebidas(reques):
    bebidas = Receta.objects.all()
    return render_to_response('lista_bebidas.html',{'lista':bebidas})

def recetas(reques):
    recetas = Receta.objects.all()
    return render_to_response('recetas.html',{'datos':recetas}, context_instance = RequestContext(reques))

def detalle_receta(reques, id_receta):
    dato = get_object_or_404(Receta, pk=id_receta)
    comentarios = Comentario.objects.filter(receta = dato)
    return render_to_response('receta.html',{'receta':dato, 'comentarios':comentarios}, context_instance=RequestContext(reques))
    
def sobre(reques):
    html = '<html><body> <h1>Acerca del Proyecto</h1><p>acerca del proyecto de recetario<br/>Proyecto de recetario de maestros del web</p></body></html>'
    return HttpResponse(html)

def inicio(reques):
    recetas = Receta.objects.all()
    return render_to_response('inicio.html',{'recetas':recetas}, context_instance = RequestContext(reques))

def usuarios(reques):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    return render_to_response('usuarios.html',{'usuarios':usuarios,'recetas':recetas}, context_instance = RequestContext(reques))

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje']+"\n"
            contenido += 'Comunicarse a:'+ formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['benllycast@gmail.com'])
            correo.send(fail_silently=False)
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
        return render_to_response('contactoform.html',{'formulario':formulario},context_instance=RequestContext(request))

def nueva_receta(request):
    if request.method == 'POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    return render_to_response('recetaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = ComentarioForm()
    return render_to_response('comentarioform.html',{'formulario':formulario}, context_instance=RequestContext(request))