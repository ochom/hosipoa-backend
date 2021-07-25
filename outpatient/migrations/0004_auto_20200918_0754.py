# Generated by Django 3.0.7 on 2020-09-18 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('outpatient', '0003_auto_20200918_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_appointment_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_appointment_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_diagnosis_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_diagnosis_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='observation',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_observation_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='observation',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_observation_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vital',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_vital_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vital',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outpatient_vital_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
