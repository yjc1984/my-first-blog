from django import forms

from .models import Post

# PostForm - Nombre del formulario que es un ModelForm
class PostForm(forms.ModelForm):

    # se le dice a Django qué modelo debe utilizar para crear este formulario (model = Post).
    class Meta:
        model = Post

        # campo(s) que se quieren en nuestro formulario. En este escenario sólo queremos title y text
        # author será la persona que se ha autenticado
        # created_date se definirá automáticamente cuando creemos un post 
        fields = ('title', 'text',)
