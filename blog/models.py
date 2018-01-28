from django.db import models
from django.utils import timezone

# models.Model especifica que la clase es un modelo de Django
# con esto se le indica a Django que debe guardarlo en la Base de datos

class Post(models.Model):
    # modelos.ForeignKey - este es un vínculo con otro modelo
    author = models.ForeignKey('auth.User')
    # models.CharField - así es como defines un texto con un número limitado de caracteres.
    title = models.CharField(max_length=200)
    # models.TextField - esto es para textos largos sin un límite
    text = models.TextField()
    # models.DateTimeField - esto es fecha y hora.
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # Método publish definido en el modelo
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Retorna el titulo del post
    def __str__(self):
        return self.title
