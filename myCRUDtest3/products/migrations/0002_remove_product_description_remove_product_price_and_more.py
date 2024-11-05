# Generated by Django 5.1.2 on 2024-11-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='jersey',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='position',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
