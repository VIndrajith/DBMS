# Generated by Django 5.1.2 on 2024-10-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='specialization',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='treatment',
            old_name='prescription',
            new_name='med',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='notes',
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
    ]
