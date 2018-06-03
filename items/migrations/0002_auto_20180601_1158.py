# Generated by Django 2.0.5 on 2018-06-01 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=68)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-number_of_clicks']},
        ),
        migrations.RemoveField(
            model_name='item',
            name='company_name',
        ),
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='Item', max_length=48),
        ),
        migrations.AlterField(
            model_name='item',
            name='number_of_clicks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itemimage',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.Item'),
        ),
        migrations.AddField(
            model_name='item',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='items.Manufacturer'),
        ),
    ]