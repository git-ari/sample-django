# Generated by Django 3.0.4 on 2020-03-29 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('checked', models.BooleanField()),
                ('order', models.IntegerField()),
                ('todoListId', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='webapp.TodoList')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
