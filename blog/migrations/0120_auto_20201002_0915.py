# Generated by Django 3.0.6 on 2020-10-02 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0119_auto_20200928_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(),
        ),
    ]