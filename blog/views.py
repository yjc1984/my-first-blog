from django.shortcuts import render
# Se importa el modelo post a la vista
from .models import Post
# Create your views here.

from django.utils import timezone

from django.shortcuts import render, get_object_or_404


#método (def) llamado post_list que toma un request y hace un return de un método render que renderizará (construirá)
#nuestra plantilla blog/post_list.html.
def post_list(request):
    # Consulta los post publicados ordenados por fecha de publicacion
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # request (todo lo que recibimos del usuario via Internet
    # archivo 'blog/post_list.html' como plantilla
    # {'posts': posts} : Se envia el post a la plantilla html
    return render(request, 'blog/post_list.html', {'posts': posts})

# Busca el post especificado en pk
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
