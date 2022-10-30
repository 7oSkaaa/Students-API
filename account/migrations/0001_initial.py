# Generated by Django 3.2.12 on 2022-10-30 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='parent.parent')),
            ],
            options={
                'db_table': 'account',
                'unique_together': {('username', 'password')},
            },
        ),
    ]
