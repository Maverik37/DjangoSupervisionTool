# Generated by Django 3.2.15 on 2023-02-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Supervision', '0006_jmeterjmx_j_resultat_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jmeterjmx',
            name='j_resultat_file',
            field=models.CharField(default='/home/fourbasse/scripts/JMETER/resultats/', max_length=200, verbose_name='Fichier'),
        ),
        migrations.AlterField(
            model_name='jmeterjmx',
            name='j_scenario_path',
            field=models.CharField(default='/home/fourbasse/scripts/JMETER/scenarios/', max_length=200, verbose_name='Path'),
        ),
    ]
