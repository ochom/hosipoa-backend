# Generated by Django 3.0.7 on 2020-09-18 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('pharmacy', '0002_auto_20200918_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispense',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_dispense', to='common.Organization'),
        ),
        migrations.AlterField(
            model_name='drug',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_drug', to='common.Organization'),
        ),
        migrations.AlterField(
            model_name='reorder',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy_reorder', to='common.Organization'),
        ),
    ]
