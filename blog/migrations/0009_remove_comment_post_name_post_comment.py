# Generated by Django 4.2.4 on 2023-09-28 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_name',
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment', verbose_name='Коментар'),
        ),
    ]
