from django.db import models

#Creating Topic class, inheriting from Model.
#Two attributes are text and date_added.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def method_unicode__(self):
        """Return a string representation of the model."""
        return self.text
