# Generated by Django 5.1.1 on 2024-10-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("note", "0006_alter_note_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="created_at",
            field=models.DateTimeField(
                auto_created=True, auto_now_add=True, verbose_name="Created at"
            ),
        ),
        migrations.AlterField(
            model_name="note",
            name="task_id",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Task ID"
            ),
        ),
    ]
