# Generated by Django 4.2.6 on 2023-10-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_alter_cavaleiro_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cavaleiro',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='assets/imagens/galeria/%Y%m'),
        ),
    ]