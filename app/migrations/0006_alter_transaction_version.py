# Generated by Django 4.1.7 on 2023-05-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_transaction_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='version',
            field=models.PositiveIntegerField(default=0, help_text='Do not touch this field', null=True),
        ),
    ]
