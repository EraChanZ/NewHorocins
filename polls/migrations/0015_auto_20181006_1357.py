# Generated by Django 2.1.1 on 2018-10-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('polls', '0014_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='potok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grad', models.CharField(default='9', max_length=100)),
                ('userr', models.CharField(default='user', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='grade',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='grade',
        ),
    ]
