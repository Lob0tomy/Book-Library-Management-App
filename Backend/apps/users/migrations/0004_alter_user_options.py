# Generated by Django 4.1.7 on 2023-04-04 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_phone_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['group']},
        ),
    ]
