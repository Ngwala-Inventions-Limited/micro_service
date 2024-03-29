# Generated by Django 4.1.7 on 2023-05-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_transaction_old_version_alter_transaction_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='date',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_trans',
            field=models.DateTimeField(help_text='Date of last Transaction', null=True, verbose_name='Last Transaction'),
        ),
    ]
