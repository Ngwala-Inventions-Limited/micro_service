# Generated by Django 4.1.7 on 2023-05-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='register',
            field=models.BooleanField(null=True),
        ),
    ]