# Generated by Django 4.2.3 on 2023-07-10 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_comment_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='image_comment',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
