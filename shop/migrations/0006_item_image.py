# Generated by Django 4.0.5 on 2022-07-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img/card_image/%Y/%m/%d'),
        ),
    ]
