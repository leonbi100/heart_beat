# Generated by Django 2.2.3 on 2019-11-27 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beat_site', '0008_auto_20191127_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imr_rate',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beat_site.Country'),
        ),
    ]
