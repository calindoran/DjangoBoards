# Generated by Django 2.1.5 on 2019-02-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("boards", "0002_topic_last_updated")]

    operations = [
        migrations.RemoveField(model_name="topic", name="last_update"),
        migrations.AddField(
            model_name="topic",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
