# Generated by Django 5.0.3 on 2024-03-23 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_funcionarios', '0003_alter_funcionario_hora_fim'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='hora_fim',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='hora_inicio',
        ),
    ]
