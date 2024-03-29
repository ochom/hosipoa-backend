# Generated by Django 3.0.7 on 2020-09-18 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bugs_bug_related', related_query_name='bugs_bugs', to='common.Organization'),
        ),
        migrations.AddField(
            model_name='replies',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bugs_replies_related', related_query_name='bugs_repliess', to='common.Organization'),
        ),
    ]
