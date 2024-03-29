# Generated by Django 3.0.7 on 2020-09-21 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20200918_0738'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('revenue', '0004_auto_20200921_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paid_date',
        ),
        migrations.CreateModel(
            name='InvoicePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount_paid', models.PositiveIntegerField(default=0)),
                ('account_name', models.CharField(max_length=250)),
                ('date_paid', models.DateField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revenue_invoicepayment_created_by', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='revenue.Invoice')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revenue_invoicepayment', to='common.Organization')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='revenue_invoicepayment_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
