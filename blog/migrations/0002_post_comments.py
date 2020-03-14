# Generated by Django 3.0.2 on 2020-03-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='post_comments', to='blog.Comment'),
        ),
    ]