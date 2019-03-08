# Generated by Django 2.1.4 on 2019-02-18 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20190217_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='lesson1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson1', to='lessons.Lesson'),
        ),
        migrations.AddField(
            model_name='topic',
            name='lesson2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lesson2', to='lessons.Lesson'),
        ),
    ]