# Generated by Django 4.1.6 on 2023-02-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_author_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages_count',
            field=models.IntegerField(null=True),
        ),
    ]
