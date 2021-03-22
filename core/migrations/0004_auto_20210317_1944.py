# Generated by Django 3.1.7 on 2021-03-17 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210317_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('track_unit', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='habit',
            old_name='track_unit',
            new_name='goal',
        ),
        migrations.AddField(
            model_name='habit',
            name='log',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.habitlog'),
        ),
    ]
