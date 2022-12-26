from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=11)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}'s message"
    

class AirdropModel(models.Model):
    INTERVAL = (
        ('select', 'Select'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('once', 'Once'),
        
    )
    url = models.URLField()
    title = models.CharField(max_length=255)
    frequency = models.CharField(max_length=10, choices=INTERVAL, default='Select')
    wallet = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    endDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
    walletCode = models.CharField(max_length=255)
    

    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-created_at',)
      
