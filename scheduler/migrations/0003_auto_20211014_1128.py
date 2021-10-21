# Generated by Django 3.2.8 on 2021-10-14 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_alter_appointment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='actions',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='afterEnd',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='beforeStart',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='color',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='content',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='isClickable',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='isDisabled',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='resizeable',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='status',
        ),
        migrations.AddField(
            model_name='appointment',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
