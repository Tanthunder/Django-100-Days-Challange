# Generated by Django 4.1.4 on 2023-01-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='number',
            field=models.CharField(blank=True, default=111, max_length=5),
            preserve_default=False,
        ),
    ]
