# Generated by Django 3.1.2 on 2022-06-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220629_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contact_id',
            field=models.IntegerField(default=-1),
        ),
    ]