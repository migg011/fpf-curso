from django.db import models

class State(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null=False)
    name = models.CharField(db_column='tx_name', null=False, blank=False, max_length=64)
    abbreviation = models.CharField(db_column='tx_abbreviation', null=False, max_length=2)

    class Meta:
        db_table = 'state'
        managed = True


class Zone(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null=False)
    name = models.CharField(db_column='tx_name', null=False, blank=False, max_length=64)

    class Meta:
        db_table = 'zone'
        managed = True


class City(models.Model):
    id = models.AutoField(db_column='id', primary_key=True, null=False)
    name = models.CharField(db_column='tx_name', null=False, blank=False, max_length=64)
    state = models.ForeignKey(db_column='id_state', to='State', on_delete=models.DO_NOTHING, null=False, related_name='cities')

    class Meta:
        db_table = 'city'
        managed = True