# Generated by Django 4.1.6 on 2023-03-16 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_book_count_sold_alter_orderlineitem_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='books',
            field=models.ManyToManyField(related_name='orders', through='books.OrderLineItem', to='books.book'),
        ),
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.country')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to='books.authorprofile'),
        ),
    ]