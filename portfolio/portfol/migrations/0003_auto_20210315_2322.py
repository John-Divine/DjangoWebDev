# Generated by Django 3.1.5 on 2021-03-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfol', '0002_auto_20210315_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfol.personalinfo'),
        ),
        migrations.AlterField(
            model_name='education',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfol.personalinfo'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfol.personalinfo'),
        ),
    ]
