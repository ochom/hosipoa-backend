# Generated by Django 3.0.7 on 2020-09-21 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20200920_1437'),
        ('revenue', '0002_auto_20200921_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='records.Patient'),
        ),
    ]
