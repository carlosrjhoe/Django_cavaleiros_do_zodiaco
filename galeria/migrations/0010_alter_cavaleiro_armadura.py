# Generated by Django 4.2.6 on 2023-10-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0009_rename_categoria_cavaleiro_armadura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cavaleiro',
            name='armadura',
            field=models.CharField(choices=[('Bronze', 'Bronze'), ('Ouro', 'Ouro'), ('Prata', 'Prata')], default='', max_length=100),
        ),
    ]