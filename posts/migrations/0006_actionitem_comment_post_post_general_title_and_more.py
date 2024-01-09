# Generated by Django 4.2.7 on 2023-12-21 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_alter_post_subcat'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('completed_flag', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'ActionItems',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_post', to='posts.post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='general_title',
            field=models.CharField(blank=True, choices=[('Others', 'Others'), ('Public_Holidays', 'Public_Holidays'), ('Process', 'Process'), ('Documentation', 'Documentation')], default='Others', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Urgent', 'Urgent')], default='Low', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, max_length=255, null=True)),
                ('action_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_created_by', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_post', to='posts.post')),
            ],
            options={
                'verbose_name_plural': 'Progresses',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ActionItemComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('actionitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_actionitem', to='posts.actionitem')),
            ],
            options={
                'verbose_name_plural': 'ActionItemComments',
            },
        ),
        migrations.AddField(
            model_name='actionitem',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actionitem_post', to='posts.post'),
        ),
    ]