# Generated by Django 4.2.1 on 2023-06-15 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_exotico_teléfono_gato_teléfono_perro_teléfono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teléfono', models.IntegerField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
    ]
