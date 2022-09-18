from django.db import models
from common.models import CommonModel

# Create your models here.


class Photo(CommonModel):

    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
