# Generated by Django 2.0.2 on 2019-07-19 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esusuaapi', '0003_auto_20190719_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esusu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esusuaapi.EsusuGroup')),
            ],
        ),
        migrations.RemoveField(
            model_name='esusumember',
            name='member',
        ),
        migrations.DeleteModel(
            name='EsusuMember',
        ),
    ]