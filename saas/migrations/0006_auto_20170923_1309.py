# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-09-23 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import saas.utils


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0005_role_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('use_amount', models.PositiveIntegerField(default=0)),
                ('extra', models.TextField(null=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='saas.Plan')),
            ],
            bases=(saas.utils.SlugTitleMixin, models.Model),
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='nb_periods',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='email',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='sync_on',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='chargeitem',
            name='invoice_key',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chargeitem',
            name='sync_on',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='plan',
            field=models.ForeignKey(help_text='item added to the cart (if plan).', null=True, on_delete=django.db.models.deletion.CASCADE, to='saas.Plan'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(0, 'created'), (3, 'disputed'), (2, 'failed'), (1, 'done')], default=0),
        ),
        migrations.AlterField(
            model_name='organization',
            name='full_name',
            field=models.CharField(blank=True, max_length=60, verbose_name='Organization name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='locality',
            field=models.CharField(max_length=50, verbose_name='City/Town'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='postal_code',
            field=models.CharField(max_length=50, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='region',
            field=models.CharField(max_length=50, verbose_name='State/Province/County'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='use',
            field=models.ForeignKey(help_text='item added to the cart (if use charge).', null=True, on_delete=django.db.models.deletion.CASCADE, to='saas.UseCharge'),
        ),
        migrations.AlterUniqueTogether(
            name='usecharge',
            unique_together=set([('slug', 'plan')]),
        ),
    ]
