# Generated by Django 3.2.4 on 2021-09-30 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=40)),
                ('cpic', models.ImageField(default='', upload_to='static/category/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=100)),
                ('ppic', models.ImageField(default='', upload_to='static/profile/')),
                ('address', models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('ppic', models.ImageField(default='', upload_to='static/products/')),
                ('color', models.CharField(max_length=12)),
                ('tprice', models.FloatField()),
                ('disprice', models.FloatField()),
                ('pdes', models.TextField(max_length=5000)),
                ('pdate', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
    ]
