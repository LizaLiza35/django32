# Generated by Django 4.2.4 on 2023-09-28 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_name',
            field=models.ForeignKey(max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Автор'),
        ),
    ]