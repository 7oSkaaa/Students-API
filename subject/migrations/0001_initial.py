# Generated by Django 3.2.12 on 2022-10-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('students', models.ManyToManyField(blank=True, related_name='subjects', to='student.Student')),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
    ]
