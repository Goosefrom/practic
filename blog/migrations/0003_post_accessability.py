# Generated by Django 2.2.3 on 2021-05-23 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='accessability',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True),
        ),
    ]
