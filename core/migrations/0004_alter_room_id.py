# Generated by Django 4.1.2 on 2022-10-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
