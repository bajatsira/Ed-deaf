# Generated by Django 4.1.7 on 2023-04-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_student_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='trueAnswer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]