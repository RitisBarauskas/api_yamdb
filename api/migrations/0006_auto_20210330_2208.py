# Generated by Django 3.0.5 on 2021-03-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210330_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='AUZSSMRL7O', max_length=10, null=True, verbose_name='confirmation code'),
        ),
    ]
