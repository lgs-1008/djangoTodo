# Generated by Django 2.2.7 on 2020-01-31 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Todo', 'verbose_name_plural': 'Todo'},
        ),
    ]