# Generated by Django 4.1.2 on 2022-10-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='total_rental',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
