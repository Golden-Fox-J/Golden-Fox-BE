# Generated by Django 4.1.5 on 2023-09-01 15:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0002_comment_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favourite_product',
            unique_together={('owner', 'Product')},
        ),
    ]
