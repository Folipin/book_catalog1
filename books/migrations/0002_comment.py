# Generated by Django 5.0.6 on 2024-05-13 16:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.book')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]