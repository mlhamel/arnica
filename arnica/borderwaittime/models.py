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
        return "<BorderWaitTime: id='%d', "\
               "office='%s', "\
               "commercial_flow='%s', "\
               "travellers_flow='%s', "\
               "updated='%s'>" % (
            self.id,
            self.office,
            self.commercial_flow,
            self.travellers_flow,
            self.updated
        )