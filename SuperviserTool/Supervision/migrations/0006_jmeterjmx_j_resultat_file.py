# Generated by Django 3.2.15 on 2023-02-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supervision', '0005_auto_20230209_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='jmeterjmx',
            name='j_resultat_file',
            field=models.CharField(default='/resultat/', max_length=200, verbose_name='Fichier'),
            preserve_default=False,
        ),
    ]