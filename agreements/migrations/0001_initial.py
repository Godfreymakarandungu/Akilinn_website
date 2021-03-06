# Generated by Django 2.1.5 on 2019-11-15 11:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Day', models.IntegerField()),
                ('Month', models.IntegerField()),
                ('Year', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=50)),
                ('Content', ckeditor.fields.RichTextField()),
                ('Picture', models.ImageField(upload_to='agreement')),
            ],
            options={
                'db_table': 'Data_Agreement',
            },
        ),
    ]
