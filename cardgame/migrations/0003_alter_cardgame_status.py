# Generated by Django 4.1.5 on 2023-01-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardgame', '0002_alter_cardgame_mode_alter_cardgame_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardgame',
            name='status',
            field=models.CharField(choices=[('끝', '끝'), ('진행 중', '진행 중')], max_length=30),
        ),
    ]
