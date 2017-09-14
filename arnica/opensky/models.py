from django.db import models


class State(models.Model):
    icao24 = models.CharField(max_length=64,
        help_text="ICAO24 address of the transmitter in hex string representation.")

    callsign = models.CharField(max_length=64,
        help_text="callsign of the vehicle. Can be None if no callsign has been received.")

    origin_country = models.CharField(max_length=64, help_text="inferred through the ICAO24 address")

    time_position = models.IntegerField(
        null=True,
        help_text="seconds since epoch of last position report. "\
                  "Can be None if there was no position report received by OpenSky within 15s before.")

    time_velocity = models.IntegerField(
        null=True,
        help_text="seconds since epoch of last velocity report. "\
                  "Can be None if there was no velocity report received by OpenSky within 15s before.")

    longitude = models.FloatField(null=True, help_text="in ellipsoidal coordinates (WGS-84) and degrees.")

    latitude = models.FloatField(null=True, help_text="in ellipsoidal coordinates (WGS-84) and degrees.")

    altitude = models.FloatField(null=True, help_text="in meters.")

    on_ground = models.BooleanField(help_text="true if aircraft is on ground (sends ADS-B surface position reports).")

    velocity = models.FloatField(help_text="over ground in m/s. Can be None if information not present")

    heading = models.FloatField(
        null=True,
        help_text="# in decimal degrees (0 is north). Can be None if information not present.")

    vertical_rate = models.FloatField(
        null=True,
        help_text="# in m/s, incline is positive, decline negative. "\
                  "Can be None if information not present.")

    sensors = models.CharField(
        max_length=64,
        null=True,
        help_text="serial numbers of sensors which received messages from the vehicle within the validity period"\
                  "of this state vector. Can be None if no filtering for sensor has been requested.")

    class Meta:
        unique_together = (("icao24", "time_position", "time_velocity"),)

    def __str__(self):
        return self.icao24

    def __repr__(self):
        return f"<State: id='{self.id}', icao24='{self.icao24}'>"