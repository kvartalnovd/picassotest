from django.db import models


class States(models.Model):
    state_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'states'

    def __str__(self) -> str:
        return f'{self.name}'


class Cities(models.Model):
    city_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.ForeignKey('States', models.CASCADE, db_column='state')

    class Meta:
        managed = True
        db_table = 'cities'

    def __str__(self) -> str:
        return f'{self.name}'
