# Generated by Django 4.1.6 on 2023-02-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
    ]
