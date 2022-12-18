# Generated by Django 4.0.6 on 2022-12-14 14:20

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('imagen_cabezera', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('titulo_tag', models.CharField(max_length=60)),
                ('cuerpo', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('descripcion', models.CharField(default='click en el link para leer mas', max_length=100)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('perfil_imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/perfil/')),
                ('Instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('github_url', models.CharField(blank=True, max_length=255, null=True)),
                ('fb_url', models.CharField(blank=True, max_length=255, null=True)),
                ('web_url', models.CharField(blank=True, max_length=255, null=True)),
                ('Twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='appblog.post')),
            ],
        ),
    ]
