# Generated by Django 3.1.3 on 2020-11-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapi', '0004_auto_20201128_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dailysales',
            fields=[
                ('sales_id', models.AutoField(primary_key=True, serialize=False)),
                ('salesdate', models.TextField(blank=True, null=True)),
                ('plnsales', models.IntegerField(blank=True, null=True)),
                ('usdsales', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'DailySales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salesorders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderdate', models.TextField(blank=True, db_column='OrderDate', null=True)),
                ('orderid', models.TextField(blank=True, db_column='OrderID', null=True)),
                ('totaldue', models.TextField(blank=True, db_column='TotalDue', null=True)),
            ],
            options={
                'db_table': 'SalesOrders',
                'managed': False,
            },
        ),
    ]
