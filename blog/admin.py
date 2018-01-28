from django.contrib import admin
# Se importa el modelo post que se creo en models.py
from .models import Post

# Se registra el modelo para hacerlo visible en la página del administrador
admin.site.register(Post)
