# Generated by Django 3.2.5 on 2023-06-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0011_auto_20230511_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='catalogo_civismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='catalogo_registro_civismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
