# Generated by Django 4.1.7 on 2023-04-09 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_user_bio_user_linkedin_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='default_space',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='default_members', to='account.space'),
        ),
    ]
