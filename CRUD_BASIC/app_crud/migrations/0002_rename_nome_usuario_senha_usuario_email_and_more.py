# Generated by Django 5.0.4 on 2024-04-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nome',
            new_name='senha',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(),
        ),
    ]