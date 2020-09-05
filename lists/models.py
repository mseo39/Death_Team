from django.db import models
from core import models as core_models
from comment import models as comment_models
# Create your models here.


class List(core_models.TimeStempedModel): # 일기 
    now = models.DateTimeField(auto_now_add=True) # 일기 날짜
#    weather = models.ImageField() # 일기 날씨
    content = models.TextField(max_length=200) # 일기 내용
    comment = models.ForeignKey(comment_models.Comment, on_delete=models.CASCADE) # 댓글 
    photos = models.ImageField(upload_to="list_photos") # 사진