# Generated by Django 4.2 on 2024-05-23 01:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_receta'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='ingredients',
            field=models.TextField(default='No especificado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flan',
            name='preparation',
            field=models.TextField(default='no especificado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flan',
            name='flan_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.DeleteModel(
            name='Receta',
        ),
    ]
