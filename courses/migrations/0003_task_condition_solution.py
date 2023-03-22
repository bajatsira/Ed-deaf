# Generated by Django 4.1.7 on 2023-03-22 17:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_longread_remove_course_body_alter_course_title_task_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='condition',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variant', to='courses.task')),
            ],
        ),
    ]
