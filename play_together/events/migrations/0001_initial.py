# Generated by Django 3.2 on 2021-04-18 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0002_alter_organization_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('is_feature', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Court name')),
            ],
            options={
                'verbose_name': 'Court',
                'verbose_name_plural': 'Courts',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Event name')),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(choices=[('ALA', 'Almaty'), ('AST', 'Astana')], default='ALA', max_length=5)),
                ('address', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organization.organization')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Team name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='events.event')),
                ('player', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='TeamWithScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='events.team')),
            ],
            options={
                'verbose_name': 'TeamWithScore',
                'verbose_name_plural': 'TeamsWithScore',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='events.category')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='games', to='events.court')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='events.event')),
                ('first_team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='first_team_games', to='events.teamwithscore')),
                ('second_team', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='second_team_games', to='events.teamwithscore')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.AddField(
            model_name='court',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courts', to='events.event'),
        ),
        migrations.AddField(
            model_name='category',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='events.event'),
        ),
    ]
