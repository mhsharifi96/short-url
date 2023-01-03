# Generated by Django 4.1.4 on 2023-01-01 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortlink', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='links',
            options={'verbose_name_plural': 'Links'},
        ),
        migrations.AddField(
            model_name='links',
            name='count_view',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Links_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_ip', models.CharField(blank=True, max_length=255, null=True)),
                ('dst_ip', models.CharField(blank=True, max_length=255, null=True)),
                ('user_agent', models.CharField(max_length=255, null=True)),
                ('cookie', models.CharField(blank=True, max_length=255, null=True)),
                ('details', models.CharField(blank=True, max_length=500, null=True)),
                ('meta_json', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shortlink.links')),
            ],
            options={
                'verbose_name_plural': 'Links log',
                'db_table': 'links_log',
            },
        ),
    ]
