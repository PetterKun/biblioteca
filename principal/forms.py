#encoding:utf-8

from django.forms import ModelForm
from django import forms
from principal.models import Obra, Video, TIPO_SEXO
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput())
    email = forms.EmailField(label="Correo electónico", widget=forms.TextInput())
    password_one = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(render_value=False))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput())
    last_name = forms.CharField(label="Apellidos", widget=forms.TextInput())
    sexo = forms.CharField(label="Sexo", widget=forms.Select(choices=TIPO_SEXO))
    dni = forms.CharField(label="DNI", widget=forms.TextInput())
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput())
    direccion = forms.CharField(label="Dirección", widget=forms.TextInput())
    cp = forms.IntegerField(label="Codigo postal", widget=forms.TextInput())
    poblacion = forms.CharField(label="Población", widget=forms.TextInput())
    provincia = forms.CharField(label="Provincia", widget=forms.TextInput())
    telefono = forms.IntegerField(label="Teléfono", widget=forms.TextInput())
    foto = forms.ImageField(label="Foto de perfil", widget=forms.FileInput())
    twitter = forms.CharField(label="Cuenta de twitter", widget=forms.TextInput())
    facebook = forms.CharField(label="Cuenta de facebook", widget=forms.TextInput())
        


