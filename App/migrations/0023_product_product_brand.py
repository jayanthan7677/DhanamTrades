# Generated by Django 4.1.7 on 2023-05-10 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_alter_feedback_feedback_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_brand',
            field=models.CharField(default='', max_length=30),
        ),
    ]
