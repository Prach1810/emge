# Generated by Django 3.0.7 on 2020-07-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200706_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='link1',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='pro1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]