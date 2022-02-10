from datetime import datetime
from django.db import models
from member.models import Member

# Create your models here.
class Fboard(models.Model):
    b_no = models.AutoField(primary_key=True)
    b_title = models.CharField(max_length=1000)
    b_content = models.TextField()
    b_date = models.DateTimeField(default=datetime.now(),blank=True)
    member = models.ForeignKey(Member,on_delete=models.DO_NOTHING,null=True)
    b_hit = models.IntegerField(default=1)
    b_img = models.ImageField(blank=True)
    
    def __str__(self):
        return self.b_title
    
    
