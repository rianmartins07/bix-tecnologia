# Generated by Django 5.0.3 on 2024-03-12 01:00

import django.db.models.deletion
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imovel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_plataforma', models.TextField(default=None, max_length=256, null=True)),
                ('taxa_plataforma', models.FloatField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
                ('imovel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='imovel.imovel')),
                ('plataforma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anuncio.plataforma')),
            ],
            options={
                'db_table': 'anuncio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HistoricalAnuncio',
            fields=[
                ('history_id', models.BigAutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, editable=False)),
                ('ultima_atualizacao', models.DateTimeField(blank=True, editable=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_relation', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='historic', to='anuncio.anuncio')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('imovel', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='imovel.imovel')),
                ('plataforma', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='anuncio.plataforma')),
            ],
            options={
                'verbose_name': 'historical anuncio',
                'verbose_name_plural': 'historical anuncios',
                'db_table': 'anuncio_historico',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
