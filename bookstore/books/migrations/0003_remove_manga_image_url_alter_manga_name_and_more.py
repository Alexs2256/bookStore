# Generated by Django 5.0.3 on 2024-04-19 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_manga_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='manga',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='manga',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='manga',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]