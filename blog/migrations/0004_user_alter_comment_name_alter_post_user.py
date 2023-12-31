# Generated by Django 4.2.4 on 2023-09-19 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Автори',
            },
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='blog.user', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.user', verbose_name='Автор'),
        ),
    ]
