# Generated by Django 4.2.7 on 2023-11-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0011_qclognote_note_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qclognote',
            name='note_details',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]