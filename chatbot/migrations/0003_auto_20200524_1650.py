# Generated by Django 3.0.6 on 2020-05-24 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatbot', '0002_auto_20200524_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('-time',)},
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
