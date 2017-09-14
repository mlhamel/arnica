from django.db import models


class Tick(models.Model):
    office = models.CharField(max_length=1000)
    commercial_flow = models.CharField(max_length=1000)
    travellers_flow = models.CharField(max_length=1000)
    updated = models.DateTimeField()

    class Meta:
        unique_together = (("office", "updated"),)

    def __str__(self):
        return self.office

    def __repr__(self):
        return f"<Tick: id='{self.id}', "\
               f"office='{self.office}', "\
               f"commercial_flow='{self.commercial_flow}', "\
               f"travellers_flow='{self.travellers_flow}', "\
               f"updated='{self.updated}'>"