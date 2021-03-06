# Generated by Django 3.2 on 2021-05-15 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Category name')),
                ('min_age', models.PositiveSmallIntegerField(default=0, verbose_name='Minimal age')),
                ('max_age', models.PositiveSmallIntegerField(default=66, verbose_name='Maximal age')),
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
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(choices=[('ALA', 'Almaty'), ('AST', 'Astana')], default='ALA', max_length=5)),
                ('address', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizations.organization')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
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
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Team name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.category')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='events.event')),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_a', models.IntegerField(default=None, null=True)),
                ('score_b', models.IntegerField(default=None, null=True)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='events.game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='team_a_games', to='events.team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='team_b_games', to='events.team'),
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
