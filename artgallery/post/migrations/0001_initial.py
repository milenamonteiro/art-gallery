# Generated by Django 3.0 on 2019-12-12 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='created at')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'Animation'), (2, 'Cartoon'), (3, 'Digital Art'), (4, 'Traditional'), (5, 'Photography'), (6, 'Caligraphy'), (7, 'Sculpture'), (8, 'Street Art'), (9, 'Characters'), (10, 'Background'), (11, 'Fantasy')])),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]