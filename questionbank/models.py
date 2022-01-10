import uuid
from django.db import models

# Create your models here.
class QuestionBank(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    question = models.CharField(max_length=300)
    optionA = models.CharField(max_length=300)
    optionB = models.CharField(max_length=300)
    optionC = models.CharField(max_length=300)
    optionD = models.CharField(max_length=300)
    correct_answer = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.question
