# Generated by Django 2.2.24 on 2021-06-29 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210629_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('IR', 'Informative'), ('KN', 'Knowledge'), ('EN', 'Entertainment')], default='EN', max_length=20),
        ),
    ]
