# Generated by Django 5.0.3 on 2024-03-17 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin', models.CharField(blank=True, db_index=True, max_length=24, unique=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('is_good', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(db_index=True)),
                ('file_path', models.FileField(blank=True, null=True, upload_to='files/')),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='django_app.agent')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to=settings.AUTH_USER_MODEL)),
                ('comment_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='django_app.comment')),
            ],
        ),
    ]
