# Generated by Django 3.0.6 on 2020-08-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0111_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
