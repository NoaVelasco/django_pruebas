# Generated by Django 5.0.1 on 2024-02-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_alter_persona_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Experiences',
            new_name='Experience',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='c_red1',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='c_red2',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='c_web',
        ),
        migrations.AddField(
            model_name='persona',
            name='rrss_1',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='rrss_2',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='web',
            field=models.URLField(blank=True),
        ),
    ]