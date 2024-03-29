# Generated by Django 4.2.7 on 2023-12-27 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_alter_jobseeker_profile_resumes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_model',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.CreateModel(
            name='jobapplyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100, null=True)),
                ('apply_resume', models.FileField(null=True, upload_to='media/apply_resume')),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.job_model')),
            ],
        ),
    ]
