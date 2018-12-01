# Generated by Django 2.0.7 on 2018-11-30 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('surname', models.CharField(max_length=25)),
                ('nickname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, upload_to='User')),
                ('date_of_birth', models.DateField(verbose_name='Дата народження')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
