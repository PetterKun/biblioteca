#encoding:utf-8
from principal.models import Obra, Video
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from principal.forms import RegistroForm, ActivacionForm, ObraForm, VideoForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from principal.funciones import *
from django.db.models import Q

def inicio(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/perfil')
    else:
        return HttpResponseRedirect('/login')

def entrar(request):
    estado = " "
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/perfil')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active and acceso.estado == 'a': 
                    login(request, acceso)
                    return HttpResponseRedirect('/perfil')
                else:
                    pin = generarPin()
                    acceso.pin = pin
                    acceso.save()
                    #titulo = 'Pin de activación - Akiba-Kei Asociación Juvenil'
                    #contenido = 'Tu pin es: ' + pin
                    #correo = EmailMessage(titulo, contenido, to=[acceso.email])
                    #correo.send()
                    return HttpResponseRedirect('/activar')
            else:
                estado = "El usuario y/o la contraseña son incorrectos."
    else:
        formulario = AuthenticationForm()
    
    return render_to_response('login.html', 
                              {
                                'formulario':formulario,
                                'estado':estado
                              },
                              context_instance=RequestContext(request)
                         )
    
@login_required(login_url='/login') 
def salir(request):
    logout(request)
    return HttpResponseRedirect('/')
    
    
@login_required(login_url='/login')            
def perfil(request):
    usuario = request.user
    return render_to_response('perfil.html', 
                              {'usuario':usuario},
                              context_instance=RequestContext(request)
                              )
    
def registro(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            email = formulario.cleaned_data['email']
            password_one = formulario.cleaned_data['password_one']
            password_two = formulario.cleaned_data['password_two']
            first_name = formulario.cleaned_data['first_name']
            last_name = formulario.cleaned_data['last_name']
            sexo = formulario.cleaned_data['sexo']
            dni = formulario.cleaned_data['dni']
            fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento']
            direccion = formulario.cleaned_data['direccion']
            cp = formulario.cleaned_data['cp']
            poblacion = formulario.cleaned_data['poblacion']
            provincia = formulario.cleaned_data['provincia']
            telefono = formulario.cleaned_data['telefono']
            foto = formulario.cleaned_data['foto']
            twitter = formulario.cleaned_data['twitter']
            facebook = formulario.cleaned_data['facebook']   
            
            u = User.objects.create_user(username=usuario, email=email, password=password_one)
            u.first_name = first_name
            u.last_name = last_name
            u.sexo = sexo
            u.dni = dni
            u.fecha_nacimiento = fecha_nacimiento
            u.direccion = direccion
            u.cp = cp
            u.poblacion = poblacion
            u.provincia = provincia
            u.telefono = telefono
            u.foto = foto
            u.twitter = twitter
            u.facebook = facebook
            
            u.save()
            
            return HttpResponseRedirect('/login')
    else:
        formulario = RegistroForm()
            
    return render_to_response('registro.html',
                              {'formulario':formulario}, 
                              context_instance=RequestContext(request))


def activacion(request):
    estado = ""
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/perfil')
    if request.method == 'POST':
        formulario = ActivacionForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            pin = formulario.cleaned_data['pin']
            acceso = authenticate(username=usuario, password=password)
            if acceso is not None:
                if acceso.pin == pin:
                    acceso.is_active = True
                    acceso.estado = 'a'
                    acceso.save()
                    return HttpResponseRedirect('/login')
                else:
                    estado = "El pin introducido es incorrecto, por favor intentelo de nuevo."
                    pin = generarPin()
                    acceso.pin = pin
                    acceso.save()
                    print pin
                    #titulo = 'Pin de activación - Akiba-Kei Asociación Juvenil'
                    #contenido = 'Tu pin es: ' + pin
                    #correo = EmailMessage(titulo, contenido, to=[acceso.email])
                    #correo.send()
            else:
                estado = "El usuario y/o la contraseña son incorrectas."
    else:
        formulario = ActivacionForm()
        
    return render_to_response('activacion.html',
                                {
                                 'formulario': formulario,
                                 'estado':estado
                                 },
                                context_instance=RequestContext(request)
                            )
                
@staff_member_required
def insertarObra(request):
    if request.method == "POST":
        formulario = ObraForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/agregarObra')
    else:
        formulario = ObraForm()
    return render_to_response('agregarobra.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request)
                              )
            
@login_required(login_url='/login')         
def buscarObra(request):
    query_q = request.GET.get('q', '')
    query_s = request.GET.get('s', '')
    if query_q and query_s:
        if query_s == 'titulo':
            qset = Q(titulo__icontains = query_q)
        elif query_s == 'autor':
            qset = Q(autor__icontains = query_q)
        elif query_s == 'editorial':
            qset = Q(editorial__icontains = query_q)
        elif query_s == 'genero':
            qset = Q(genero__icontains = query_q)
        elif query_s == 'palabra_clave':
            qset = Q(palabra_clave__icontains = query_q)
        resultados = Obra.objects.filter(qset)
    else:
        resultados = []
        
    return render_to_response('busquedaObra.html',
                              {
                                'resultados':resultados,
                                'query_q':query_q,
                                'query_s':query_s
                               },
                              context_instance=RequestContext(request)
                              )      
    
    
def detalleObra(request, id_obra):
    dato = get_object_or_404(Obra, pk=id_obra)
    return render_to_response('obra.html', 
                              {'obra':dato},
                              context_instance=RequestContext(request)                      
    )    