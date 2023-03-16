# Generated by Django 4.1.7 on 2023-03-16 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_work', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('patronymic', models.CharField(max_length=25)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.work')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(max_length=20)),
                ('add_order', models.DateTimeField()),
                ('cost', models.IntegerField(max_length=10)),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.status')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.worker')),
            ],
        ),
    ]
