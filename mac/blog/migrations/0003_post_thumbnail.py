# Generated by Django 3.1.7 on 2021-03-10 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210310_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
