# Generated by Django 4.1.7 on 2023-05-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='old_version',
            field=models.PositiveIntegerField(default=0, help_text='Do not touch this field', null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='version',
            field=models.PositiveIntegerField(default=1, help_text='Do not touch this field', null=True),
        ),
    ]
