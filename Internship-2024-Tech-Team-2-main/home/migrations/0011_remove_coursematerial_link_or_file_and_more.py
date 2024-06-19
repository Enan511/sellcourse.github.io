# Generated by Django 5.0.4 on 2024-04-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_coursematerial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursematerial',
            name='link_or_file',
        ),
        migrations.RemoveField(
            model_name='coursematerial',
            name='material_type',
        ),
        migrations.AddField(
            model_name='coursematerial',
            name='file',
            field=models.FileField(default='default.pdf', upload_to='course_materials/'),
        ),
        migrations.AddField(
            model_name='coursematerial',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
