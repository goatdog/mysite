# Generated by Django 3.2.25 on 2024-07-31 11:26

import catalog.constants
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On_loan'), ('a', 'Available'), ('r', 'Reserved')], default=catalog.constants.LoanStatus['MAINTENANCE'], help_text='Book Availability', max_length=1),
        ),
    ]
