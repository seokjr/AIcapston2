# Generated by Django 4.1.3 on 2022-11-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0004_alter_answer_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.IntegerField(null=True),
        ),
    ]