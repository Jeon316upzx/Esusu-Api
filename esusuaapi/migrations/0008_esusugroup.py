# Generated by Django 2.0.2 on 2019-07-20 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esusuaapi', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='EsusuGroup',
            fields=[
                ('group_uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group_limit', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amount_to_save', models.IntegerField()),
                ('is_public', models.BooleanField()),
                ('g_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
    ]