# Generated by Django 4.0.4 on 2022-07-01 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0005_alter_invitation_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='answered',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
