# Generated by Django 4.2.9 on 2024-01-03 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('nickname', models.AutoField(primary_key=True, serialize=False)),
                ('puuid', models.TextField(max_length=30)),
                ('tagLine', models.TextField(max_length=30)),
                ('id', models.TextField(max_length=100)),
                ('profileIconId', models.TextField(max_length=30)),
                ('summonerLevel', models.TextField(max_length=30)),
                ('tier', models.TextField(max_length=30)),
                ('leaguePoints', models.TextField(max_length=30)),
                ('queueType', models.TextField(max_length=30)),
                ('rank', models.TextField(max_length=30)),
                ('wins', models.TextField(max_length=30)),
                ('losses', models.TextField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
