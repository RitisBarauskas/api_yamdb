# Generated by Django 3.0.5 on 2021-03-28 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210326_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='MJ1EC3CYWP1ADGJDM3MYMJVN2GWNMR', max_length=30, null=True, verbose_name='confirmation code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Администратор'), ('moderator', 'Модератор'), ('user', 'Пользователь')], default='user', max_length=30, null=True, verbose_name='role'),
        ),
    ]
