# Generated by Django 3.2 on 2021-05-04 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
