# Generated by Django 3.0.1 on 2020-01-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_auto_20200124_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='jsonFile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
