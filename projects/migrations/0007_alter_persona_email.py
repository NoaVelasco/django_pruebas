# Generated by Django 5.0.1 on 2024-02-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_rename_c_email_persona_email_remove_persona_exp1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]