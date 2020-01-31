from django.db import models
# Create your models here.

class Todo(models.Model):

    createUser = models.CharField(max_length = 50, default='')
    todoText = models.CharField(max_length=150, null = False)
    createDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'
        ordering = ['createDate']


    def __str__(self):
        return self.todoText
