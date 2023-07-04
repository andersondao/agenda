# Generated by Django 4.2 on 2023-04-17 23:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(blank=True, max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('descricao', models.TextField(blank=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contatos.categoria')),
            ],
        ),
    ]
