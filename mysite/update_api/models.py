from django.db import models

class Notifications(models.Model):
    """This class represents the bucketlist model."""
    title = models.CharField(max_length=200)
    read_status = models.BooleanField(default=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)
