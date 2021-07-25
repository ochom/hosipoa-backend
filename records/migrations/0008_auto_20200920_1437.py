# Generated by Django 3.0.7 on 2020-09-20 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20200918_0838'),
        ('records', '0007_auto_20200920_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientinsurance',
            name='company_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.Insurance'),
        ),
        migrations.AlterField(
            model_name='patientinsurance',
            name='patient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_insurances', to='records.Patient'),
        ),
    ]
