# Generated by Django 3.0.7 on 2020-09-18 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('laboratory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logbook',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laboratory_logbook_related', related_query_name='laboratory_logbooks', to='common.Organization'),
        ),
    ]
