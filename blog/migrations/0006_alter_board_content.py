# Generated by Django 4.1.3 on 2022-11-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_board_bigtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='content',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
