# Generated by Django 3.2.2 on 2021-06-19 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=160)),
            ],
            options={
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=20)),
                ('company', models.CharField(default='', max_length=80)),
                ('address', models.CharField(default='', max_length=70)),
                ('city', models.CharField(default='', max_length=40)),
                ('state', models.CharField(default='', max_length=40)),
                ('country', models.CharField(default='', max_length=40)),
                ('postal_code', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=24)),
                ('fax', models.CharField(default='', max_length=24)),
                ('email', models.EmailField(db_index=True, default='', max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_date', models.DateTimeField(db_index=True)),
                ('billing_address', models.CharField(default='', max_length=70)),
                ('billing_city', models.CharField(default='', max_length=40)),
                ('billing_state', models.CharField(default='', max_length=40)),
                ('billing_country', models.CharField(default='', max_length=40)),
                ('billing_postal_code', models.CharField(default='', max_length=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jampy.customer')),
            ],
            options={
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Media Types',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('composer', models.CharField(db_index=True, max_length=220, null=True)),
                ('msec', models.IntegerField(default=0)),
                ('bytes', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='jampy.album')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='jampy.genre')),
                ('media_type', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='jampy.mediatype')),
            ],
            options={
                'verbose_name_plural': 'Tracks',
            },
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('quantity', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jampy.invoice')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jampy.track')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=20)),
                ('title', models.CharField(default='', max_length=30)),
                ('birth_date', models.DateTimeField(null=True)),
                ('hire_date', models.DateTimeField(null=True)),
                ('address', models.CharField(default='', max_length=70)),
                ('city', models.CharField(default='', max_length=40)),
                ('state', models.CharField(default='', max_length=40)),
                ('country', models.CharField(default='', max_length=40)),
                ('postal_code', models.CharField(default='', max_length=10)),
                ('phone', models.CharField(default='', max_length=24)),
                ('fax', models.CharField(default='', max_length=24)),
                ('email', models.EmailField(db_index=True, default='', max_length=254)),
                ('reports_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='jampy.employee')),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='support',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='jampy.employee', verbose_name='Support'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jampy.artist'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['first_name', 'last_name'], name='jampy_emplo_first_n_2067af_idx'),
        ),
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['first_name', 'last_name'], name='jampy_custo_first_n_62fb0a_idx'),
        ),
    ]
