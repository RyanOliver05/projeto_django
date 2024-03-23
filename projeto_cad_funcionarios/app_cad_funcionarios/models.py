from django.db import models

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    cargo = models.TextField(max_length=255)

    def save(self, *args, **kwargs):
        if Funcionario.objects.filter(nome=self.nome, cargo=self.cargo).exists():
            pass
        else:
            super(Funcionario, self).save(*args, **kwargs)
    