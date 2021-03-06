# Generated by Django 3.2.9 on 2022-02-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modem', '0002_alter_amtcmodel_sn'),
    ]

    operations = [
        migrations.AddField(
            model_name='amtcmodel',
            name='p2',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15')], max_length=100, null=True, verbose_name='PORT'),
        ),
        migrations.AddField(
            model_name='amtcmodel',
            name='p3',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19')], max_length=100, null=True, verbose_name='ONT'),
        ),
        migrations.AddField(
            model_name='amtcmodel',
            name='vlan',
            field=models.IntegerField(blank=True, choices=[('701', '701'), ('702', '702'), ('703', '703'), ('704', '704'), ('705', '705'), ('706', '706'), ('707', '707'), ('708', '708'), ('709', '709'), ('710', '710')], default=700, null=True, verbose_name='VLAN'),
        ),
        migrations.AlterField(
            model_name='amtcmodel',
            name='p1',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19')], max_length=100, null=True, verbose_name='PLATA'),
        ),
    ]
