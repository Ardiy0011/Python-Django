# Generated by Django 4.0.3 on 2022-12-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_delete_storesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulist',
            name='image',
            field=models.ImageField(upload_to='media/menu_images/'),
        ),
    ]