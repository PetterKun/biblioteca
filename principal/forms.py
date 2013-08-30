#encoding:utf-8

from django.forms import ModelForm
from django import forms
from principal.models import Obra, Video, TIPO_SEXO, TIPO_BUSQUEDA_OBRA, TIPO_DE_OBRA
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput())
    email = forms.EmailField(label="Correo electónico", widget=forms.TextInput())
    password_one = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(render_value=False))
    first_name = forms.CharField(required=False, label="Nombre", widget=forms.TextInput())
    last_name = forms.CharField(required=False, label="Apellidos", widget=forms.TextInput())
    sexo = forms.CharField(required=False, label="Sexo", widget=forms.Select(choices=TIPO_SEXO))
    dni = forms.CharField(required=False, label="DNI", widget=forms.TextInput())
    fecha_nacimiento = forms.DateField(required=False, label="Fecha de nacimiento", widget=forms.DateInput())
    direccion = forms.CharField(required=False, label="Dirección", widget=forms.TextInput())
    cp = forms.IntegerField(required=False, label="Codigo postal", widget=forms.TextInput())
    poblacion = forms.CharField(required=False, label="Población", widget=forms.TextInput())
    provincia = forms.CharField(required=False, label="Provincia", widget=forms.TextInput())
    telefono = forms.IntegerField(required=False, label="Teléfono", widget=forms.TextInput())
    foto = forms.ImageField(required=False, label="Foto de perfil", widget=forms.FileInput())
    twitter = forms.CharField(required=False, label="Cuenta de twitter", widget=forms.TextInput())
    facebook = forms.CharField(required=False, label="Cuenta de facebook", widget=forms.TextInput())
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('El nombre de usuario ya existe.')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('El email ya está registrado.')
    
    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']
        if password_one == password_two:
            pass
        else:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        
    def clean_dni(self):
        dni = self.cleaned_data['dni']
        try:
            u = User.objects.get(dni=dni)
        except User.DoesNotExist:
            return dni
        raise forms.ValidationError('El DNI introducido ya existe.')
    

class ActivacionForm(forms.Form):
    username = forms.CharField(label="Usuario", widget=forms.TextInput())
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(render_value=False))
    pin = forms.IntegerField(label="Pin de validación", widget=forms.TextInput())
    
            
class ObraForm(ModelForm):
    class Meta:
        model = Obra
        
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        try:
            obra = Obra.objects.get(codigo=codigo)
        except Obra.DoesNotExist:
            return codigo
        raise forms.ValidationError("El código introducido ya existe.")
    
    
class VideoForm(ModelForm):
    class Meta:
        model = Video