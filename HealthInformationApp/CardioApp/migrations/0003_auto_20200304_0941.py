# Generated by Django 3.0.3 on 2020-03-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardioApp', '0002_auto_20200304_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='visit_date',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
