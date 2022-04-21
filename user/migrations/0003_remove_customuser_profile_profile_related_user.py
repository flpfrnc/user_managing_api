# Generated by Django 4.0.4 on 2022-04-19 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='related_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.customuser'),
        ),
    ]