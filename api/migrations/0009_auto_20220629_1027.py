# Generated by Django 3.1.2 on 2022-06-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220629_0318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='contacts',
        ),
        migrations.AddField(
            model_name='person',
            name='contacts',
            field=models.ManyToManyField(blank=True, db_constraint=False, null=True, to='api.Contact'),
        ),
    ]
