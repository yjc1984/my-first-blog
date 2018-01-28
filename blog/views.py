from django.shortcuts import render
# Se importa el modelo post a la vista
from .models import Post
# Para la hora local
from django.utils import timezone
# Metodo render y para Page not found
from django.shortcuts import render, get_object_or_404
# Para hacer redirecciones
from django.shortcuts import redirect
# Para crear formularios
from .forms import PostForm


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

# Vista del formulario
def post_new(request):
    #En nuestra view tenemos dos posibles situaciones a contemplar.
    #Primero: cuando accedemos a la página por primera vez y queremos un formulario en blanco.
    #Segundo: cuando volvemos a la view con los datos del formulario que acabamos de escribir
    if request.method == "POST":
        #Si el method es POST queremos construir el PostForm con los datos del formulario
        form = PostForm(request.POST)
        #verificar si el formulario es correcto (todos los campos necesarios están definidos y no hay valores incorrectos)
        if form.is_valid():
            #Guardar formulario. commit=False significa que no queremos guardar el modelo Post todavía
            #queremos añadir el autor primero
            post = form.save(commit=False)
            #Añadir autor
            post.author = request.user
            #Fecha del post
            post.published_date = timezone.now()
            #post.save() conservará los cambios (añadiendo el autor) y se creará una nuevo post en el blog.
            post.save()
            #Redirecciona a la pagina post_detail
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# Vista para editar un post
# pasamos un parámetro extra pk de los urls
def post_edit(request, pk):
    # obtenemos el modelo Post que queremos editar con get_object_or_404(Post, pk=pk)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # pasamos este post como una instancia para guardar el formulario
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # pasamos este post como una instancia para editar el formulario
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
