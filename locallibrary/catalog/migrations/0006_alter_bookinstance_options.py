# Generated by Django 3.2.25 on 2024-07-29 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('add_author', 'Add author to the library'), ('change author', 'Update author'), ('delete author', 'Delete author'))},
        ),
    ]
