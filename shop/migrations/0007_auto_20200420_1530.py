# Generated by Django 3.0.2 on 2020-04-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='magt_id',
            new_name='msg_id',
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=300),
        ),
    ]
