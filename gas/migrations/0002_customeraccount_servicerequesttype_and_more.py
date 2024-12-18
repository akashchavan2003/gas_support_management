# Generated by Django 5.1.2 on 2024-11-30 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('account_number', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequestType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='details',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='date_resolved',
            new_name='resolved_at',
        ),
        migrations.RenameField(
            model_name='servicerequest',
            old_name='date_submitted',
            new_name='submitted_at',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='user',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='customer_email',
            field=models.EmailField(default='unknown@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='customer_name',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='customer_phone',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='support_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='service_request_attachments/'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('RESOLVED', 'Resolved'), ('CANCELLED', 'Cancelled')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='request_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gas.servicerequesttype'),
        ),
    ]
