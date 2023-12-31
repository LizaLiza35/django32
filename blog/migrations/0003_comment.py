# Generated by Django 4.2.4 on 2023-09-19 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_post_options_post_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='Дата та час')),
                ('description', models.TextField(max_length=300, verbose_name='Коментар')),
                ('name', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментарі',
            },
        ),
    ]
