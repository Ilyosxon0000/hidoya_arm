# Generated by Django 4.2.4 on 2023-11-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_book_code_number_book_location_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='location_book',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='kitob joylashuvi'),
        ),
    ]
