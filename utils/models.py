from django.db import models

class BaseModelManager(models.Manager):
    def exists(self, **params):
        return self.filter(**params).count()

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_on']
        get_latest_by = 'created_on'
        
    def update(self, **attributes):
        for attr_name in attributes:
            setattr(self, attr_name, attributes[attr_name])
        self.save()
