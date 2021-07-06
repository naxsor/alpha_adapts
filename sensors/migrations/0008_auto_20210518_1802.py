# Generated by Django 3.1.3 on 2021-05-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0007_auto_20210513_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_1',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_10',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_11',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_12',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_13',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_14',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_15',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_16',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_17',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_18',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_19',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_2',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_20',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_21',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_22',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_23',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_24',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_25',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_26',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_27',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_28',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_29',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_3',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_30',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_31',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_32',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_33',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_34',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_35',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_36',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_37',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_38',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_39',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_4',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_40',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_41',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_42',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_43',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_44',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_45',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_46',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_47',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_48',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_49',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_5',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_50',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_51',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_52',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_53',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_54',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_55',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_56',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_57',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_58',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_59',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_6',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_60',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_7',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_8',
        ),
        migrations.RemoveField(
            model_name='dma',
            name='bin_constant_9',
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_1',
            field=models.FloatField(blank=True, db_column='Bin Concentration 1', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_10',
            field=models.FloatField(blank=True, db_column='Bin Concentration 10', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_11',
            field=models.FloatField(blank=True, db_column='Bin Concentration 11', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_12',
            field=models.FloatField(blank=True, db_column='Bin Concentration 12', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_13',
            field=models.FloatField(blank=True, db_column='Bin Concentration 13', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_14',
            field=models.FloatField(blank=True, db_column='Bin Concentration 14', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_15',
            field=models.FloatField(blank=True, db_column='Bin Concentration 15', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_16',
            field=models.FloatField(blank=True, db_column='Bin Concentration 16', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_17',
            field=models.FloatField(blank=True, db_column='Bin Concentration 17', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_18',
            field=models.FloatField(blank=True, db_column='Bin Concentration 18', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_19',
            field=models.FloatField(blank=True, db_column='Bin Concentration 19', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_2',
            field=models.FloatField(blank=True, db_column='Bin Concentration 2', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_20',
            field=models.FloatField(blank=True, db_column='Bin Concentration 20', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_21',
            field=models.FloatField(blank=True, db_column='Bin Concentration 21', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_22',
            field=models.FloatField(blank=True, db_column='Bin Concentration 22', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_23',
            field=models.FloatField(blank=True, db_column='Bin Concentration 23', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_24',
            field=models.FloatField(blank=True, db_column='Bin Concentration 24', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_25',
            field=models.FloatField(blank=True, db_column='Bin Concentration 25', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_26',
            field=models.FloatField(blank=True, db_column='Bin Concentration 26', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_27',
            field=models.FloatField(blank=True, db_column='Bin Concentration 27', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_28',
            field=models.FloatField(blank=True, db_column='Bin Concentration 28', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_29',
            field=models.FloatField(blank=True, db_column='Bin Concentration 29', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_3',
            field=models.FloatField(blank=True, db_column='Bin Concentration 3', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_30',
            field=models.FloatField(blank=True, db_column='Bin Concentration 30', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_31',
            field=models.FloatField(blank=True, db_column='Bin Concentration 31', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_32',
            field=models.FloatField(blank=True, db_column='Bin Concentration 32', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_33',
            field=models.FloatField(blank=True, db_column='Bin Concentration 33', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_34',
            field=models.FloatField(blank=True, db_column='Bin Concentration 34', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_35',
            field=models.FloatField(blank=True, db_column='Bin Concentration 35', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_36',
            field=models.FloatField(blank=True, db_column='Bin Concentration 36', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_37',
            field=models.FloatField(blank=True, db_column='Bin Concentration 37', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_38',
            field=models.FloatField(blank=True, db_column='Bin Concentration 38', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_39',
            field=models.FloatField(blank=True, db_column='Bin Concentration 39', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_4',
            field=models.FloatField(blank=True, db_column='Bin Concentration 4', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_40',
            field=models.FloatField(blank=True, db_column='Bin Concentration 40', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_41',
            field=models.FloatField(blank=True, db_column='Bin Concentration 41', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_42',
            field=models.FloatField(blank=True, db_column='Bin Concentration 42', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_43',
            field=models.FloatField(blank=True, db_column='Bin Concentration 43', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_44',
            field=models.FloatField(blank=True, db_column='Bin Concentration 44', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_45',
            field=models.FloatField(blank=True, db_column='Bin Concentration 45', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_46',
            field=models.FloatField(blank=True, db_column='Bin Concentration 46', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_47',
            field=models.FloatField(blank=True, db_column='Bin Concentration 47', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_48',
            field=models.FloatField(blank=True, db_column='Bin Concentration 48', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_49',
            field=models.FloatField(blank=True, db_column='Bin Concentration 49', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_5',
            field=models.FloatField(blank=True, db_column='Bin Concentration 5', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_50',
            field=models.FloatField(blank=True, db_column='Bin Concentration 50', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_51',
            field=models.FloatField(blank=True, db_column='Bin Concentration 51', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_52',
            field=models.FloatField(blank=True, db_column='Bin Concentration 52', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_53',
            field=models.FloatField(blank=True, db_column='Bin Concentration 53', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_54',
            field=models.FloatField(blank=True, db_column='Bin Concentration 54', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_55',
            field=models.FloatField(blank=True, db_column='Bin Concentration 55', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_56',
            field=models.FloatField(blank=True, db_column='Bin Concentration 56', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_57',
            field=models.FloatField(blank=True, db_column='Bin Concentration 57', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_58',
            field=models.FloatField(blank=True, db_column='Bin Concentration 58', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_59',
            field=models.FloatField(blank=True, db_column='Bin Concentration 59', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_6',
            field=models.FloatField(blank=True, db_column='Bin Concentration 6', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_60',
            field=models.FloatField(blank=True, db_column='Bin Concentration 60', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_7',
            field=models.FloatField(blank=True, db_column='Bin Concentration 7', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_8',
            field=models.FloatField(blank=True, db_column='Bin Concentration 8', null=True),
        ),
        migrations.AddField(
            model_name='dma',
            name='bin_conc_9',
            field=models.FloatField(blank=True, db_column='Bin Concentration 9', null=True),
        ),
    ]