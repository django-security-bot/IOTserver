# Generated by Django 4.0.1 on 2022-06-20 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_session_session_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.TextField()),
                ('device_name', models.TextField()),
                ('ip_address', models.GenericIPAddressField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_account', to='web.u')),
            ],
        ),
    ]
