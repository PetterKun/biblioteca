#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

#############################################  TIPOS DE DATOS  ##############################################

TIPO_DE_OBRA = (
                    ('ce', 'Cómic Europeo'),
                    ('ca', 'Cómic Americano'),
                    ('cs', 'Cómic Español'),
                    ('mg', 'Manga'),
                    ('mw', 'Manhwa'),
                    ('lb', 'Libro'),
                    ('ng', 'Novela Gráfica'),
                )

PLATAFORMA_DE_VIDEO = (
                    ('vhs', 'VHS'),
                    ('dvd', 'DVD'),
                    ('ray', 'BLUE-RAY'),
                 )

TIPO_EDAD = (
                ('tp', 'Todos los Públicos'),
                ('+7', 'Mayores de 7 años'),
                ('+12', 'Mayores de 12 años'),
                ('+16', 'Mayores de 16 años'),
                ('+18', 'Mayores de 18 años'),
                ('+X', 'Clasificación para adultos'),
             )


TIPO_ESTADO = (
                ('d','Disponible'),
                ('p', 'Prestado'),
                ('c', 'Solo consultas'),
               )

TIPO_SEXO = (
                ('h', 'Hombre'),
                ('m', 'Mujer'),
             )

TIPO_USUARIO = (
                    ('s', 'Socio'),
                    ('n', 'No socio'),
                    ('p', 'Presidencia'),
                    ('v', 'Vicepresidencia'),
                    ('s', 'Secretaría'),
                    ('t', 'Tesorería'),
                    ('a', 'Administrador'),
                )

ESTADO_CUENTA = (
                    ('a', 'Activada'),
                    ('d', 'Desactivada'),
                    ('b', 'Bloqueada'),
                    ('s', 'Suspendida'),
                 )
#############################################  Clase RECURSO  ##################################################
##                             Clase genérica para los tipos de datos a añadir                                ##
################################################################################################################

User.add_to_class('dni', models.CharField(blank=True, verbose_name="DNI", max_length=9))
User.add_to_class('sexo', models.CharField(blank=False, verbose_name="Sexo", max_length=1, choices=TIPO_SEXO))
User.add_to_class('fecha_nacimiento', models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento"))
User.add_to_class('tipo_usuario', models.CharField(blank=False, verbose_name="Tipo de Usuario", max_length=1, choices=TIPO_USUARIO, default='n'))
User.add_to_class('direccion', models.CharField(blank=True, verbose_name="Dirección", max_length=100))
User.add_to_class('cp', models.IntegerField(null=True, blank=True, verbose_name="Código postal"))
User.add_to_class('poblacion', models.CharField(blank=True, verbose_name="Población", max_length=50))
User.add_to_class('provincia', models.CharField(blank=True, verbose_name="Provincia", max_length=20))
User.add_to_class('telefono', models.IntegerField(null=True, blank=True, verbose_name="Teléfono"))
User.add_to_class('foto', models.ImageField(blank=True, upload_to='foto_perfil', verbose_name="Fotografía"))
User.add_to_class('estado', models.CharField(blank=False, max_length=1, verbose_name="Estado de la cuenta", choices=ESTADO_CUENTA, default='d'))
User.add_to_class('twitter', models.CharField(blank=True, max_length=20, verbose_name="Cuenta de Twitter"))
User.add_to_class('facebook', models.CharField(blank=True, max_length=50, verbose_name="Cuenta de Facebook"))
User.add_to_class('pin', models.IntegerField(null=False, max_length=4, verbose_name="Pin de verificación", default=0))


#############################################  Clase RECURSO  ##################################################
##                             Clase genérica para los tipos de datos a añadir                                ##
################################################################################################################

class Recurso(models.Model):
    codigo = models.CharField(blank=False, null=False ,max_length=15, verbose_name="Código de identificación", help_text="Codigo de identificación de la Biblioteca. Ej: MA/KINA/31-11.")
    genero = models.CharField(blank=False, max_length=15, verbose_name="Género", help_text="Género de la obra.")
    subgenero = models.CharField(blank=True, max_length=15, verbose_name="Subgénero", help_text="Subgénero de la obra.")
    titulo = models.CharField(blank=False, max_length=100, verbose_name="Título", help_text="Título de la obra.")
    volumen = models.IntegerField(blank=False, verbose_name="Volumen")
    nCopia = models.IntegerField(blank=False, verbose_name="Número de Copia")
    anyo = models.IntegerField(blank=False, verbose_name="Año")
    edad = models.CharField(blank=False, max_length=3, verbose_name="Edad recomendada", choices=TIPO_EDAD)
    idioma = models.CharField(blank=False, max_length=15, verbose_name="Idioma")
    palabra_clave = models.CharField(blank=False, null=False, max_length=100, verbose_name="Palabra Clave")
    resumen = models.TextField(blank=True, verbose_name="Resumen", help_text="Resumen de la obra.")
    fecha_add = models.DateTimeField(auto_now=True)
    estado = models.CharField(blank=False, max_length=1, verbose_name="Estado", choices=TIPO_ESTADO)
    imagen = models.ImageField(upload_to='imagenes_obras', blank=True, verbose_name="Fotografía")
    
    def __unicode__(self):
        return u"%s," % self.titulo
        
        
#############################################  Clase OBRA  #####################################################
##                             Clase para almacenar libros, comics, etc...                                    ##
################################################################################################################        
    
class Obra(Recurso):
    tipo = models.CharField(blank=False ,max_length=2, verbose_name="Tipo", choices=TIPO_DE_OBRA)
    autor = models.CharField(blank=False, max_length=50, verbose_name="Autor", help_text="Autor de la obra.")
    editorial = models.CharField(blank=False, max_length=50, verbose_name="Editorial", help_text="Editorial de la obra.")
    nEdicion = models.IntegerField(blank=False, verbose_name="Número de Edición")
    isbn = models.IntegerField(blank=False, max_length=13, verbose_name="ISBN")


#############################################  Clase VIDEO  ####################################################
##                             Clase para almacenar películas, animes, ovas, etc                              ##
################################################################################################################

class Video(Recurso):
    plataforma = models.CharField(blank=False, max_length=3, verbose_name="Plataforma", choices=PLATAFORMA_DE_VIDEO)
    codigo_distribucion = models.IntegerField(blank=False, max_length=13, verbose_name="Codigo de Distribución")
    tipo = models.CharField(blank=False, max_length=15, verbose_name="Tipo", help_text="Tipo de video: animacion, imagen real, digital, etc...")
    subtipo = models.CharField(blank=False, max_length=15, verbose_name="Subtipo", help_text="Subtipo de video: anime, pelicula, ova, etc...")
    director = models.CharField(blank=False, max_length=50, verbose_name="Director")
    productora = models.CharField(blank=False, max_length=50, verbose_name="Productora")

    

    
    
    
    
    
    
    
    
    
    
    
    
    