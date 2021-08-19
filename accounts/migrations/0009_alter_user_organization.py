# Generated by Django 3.2.5 on 2021-08-22 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20200918_0738'),
        ('accounts', '0008_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='common.organization'),
        ),
    ]
