# Generated by Django 3.2.9 on 2022-01-02 20:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycineomatica', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_detail',
            name='film',
        ),
        migrations.RemoveField(
            model_name='cart_detail',
            name='quantity',
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(20)])),
                ('row', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(13)])),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mycineomatica.film')),
            ],
        ),
        migrations.AddField(
            model_name='cart_detail',
            name='ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='mycineomatica.ticket'),
            preserve_default=False,
        ),
    ]