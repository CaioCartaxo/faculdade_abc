from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nascimento = models.CharField(max_length=11, blank=True, null=True)
    profissao = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    celular = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    n_endereco = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Cursos_Bacharel(models.Model):
    n_curso = models.CharField(max_length=10, unique=True)
    data_curso = models.CharField(max_length=10)
    periodos_curso = models.CharField(max_length=5)
    valor_curso = models.CharField(max_length=10)


class Inscrito_Curso_Bacharel(models.Model):
    aluno = models.CharField(max_length=100)
    data_inscricao = models.DateField(auto_now=True)
    curso_inscrito = models.CharField(max_length=10)
    pago = models.BooleanField(default=False)
    pago_em = models.DateField(null=True)