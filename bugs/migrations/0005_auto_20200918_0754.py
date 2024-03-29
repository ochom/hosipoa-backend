# Generated by Django 3.0.7 on 2020-09-18 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0004_auto_20200918_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bugs_bug_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bug',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bugs_bug_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='replies',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bugs_replies_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='replies',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bugs_replies_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
