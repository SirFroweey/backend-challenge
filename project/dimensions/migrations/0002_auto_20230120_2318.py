# Generated by Django 3.0.5 on 2023-01-20 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dimensions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dimension',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='dimension',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subdimensions', to='dimensions.Dimension'),
        ),
    ]
