# Generated by Django 4.2.4 on 2023-11-15 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('topshirilgan', 'Topshirilgan'), ('topshirilmagan', 'Topshirilmagan')], default='topshirilmagan', max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.book')),
            ],
        ),
    ]