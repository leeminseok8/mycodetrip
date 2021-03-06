# Generated by Django 4.0.1 on 2022-01-13 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100, unique=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_tickets', models.IntegerField()),
                ('payments_method', models.CharField(default='카드', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=50)),
                ('given_name', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=20)),
                ('birthday', models.DateTimeField()),
                ('flight_seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flightseat')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
    ]
