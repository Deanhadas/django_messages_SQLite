from django.db import models

class Message(models.Model):

    sender = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    message = models.CharField(max_length=3000)
    subject = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __json__(self):
        return {"sender":self.sender,
                "receiver": self.receiver,
                "message": self.message,
                "subject": self.subject,
                "creation_date": self.creation_date.strftime('%Y-%m-%d %H:%M:%S'),
                "is_read": self.is_read,
                }