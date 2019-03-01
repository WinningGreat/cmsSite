# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-23 00:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0004_auto_20170411_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='digital_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_rating', models.IntegerField()),
                ('item_price', models.FloatField()),
                ('item_image', models.ImageField(upload_to='item/images')),
                ('item_status', models.CharField(choices=[('AVAILABLE', 'A/V'), ('NOT AVAILABLE', 'N/A')], max_length=255)),
                ('number_of_downloads', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='physical_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_rating', models.IntegerField()),
                ('item_price', models.FloatField()),
                ('item_image', models.ImageField(upload_to='item/images')),
                ('item_status', models.CharField(choices=[('AVAILABLE', 'A/V'), ('NOT AVAILABLE', 'N/A')], max_length=255)),
                ('item_weight', models.FloatField()),
                ('shipping_cost', models.FloatField()),
                ('item_state', models.CharField(choices=[('Item is new', 'new'), ('Item has been refurbished', 'refurbished'), ('Item is fairly used', 'used')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AddField(
            model_name='physical_item',
            name='SalePage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moderna.SalePage'),
        ),
        migrations.AddField(
            model_name='digital_item',
            name='SalePage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moderna.SalePage'),
        ),
    ]
