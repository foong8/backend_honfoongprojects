# Generated by Django 4.2.7 on 2023-11-24 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations', '0004_remove_assignment_country_assignment_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='qclog',
            name='qcresult',
            field=models.CharField(choices=[('No_Error', 'No_Error'), ('Has_Error', 'Has_Error')], default='No_Error', max_length=255),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aaa', to='operations.country'),
        ),
        migrations.AlterField(
            model_name='qclog',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending_Update', 'Pending_Update'), ('Pending_Approve', 'Pending_Approve'), ('Submit_To_Cancel', 'Submit_To_Cancel'), ('Cancelled_Approved', 'Cancelled_Approved')], default='Completed', max_length=255),
        ),
        migrations.CreateModel(
            name='QCLogNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_qclognote', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_qclognote', to=settings.AUTH_USER_MODEL)),
                ('qclog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qclog', to='operations.qcticket')),
            ],
        ),
    ]