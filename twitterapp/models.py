from django.db import models


class RequestLog(models.Model):
    request_log = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.request_log)


class Tweet(models.Model):
    text = models.TextField()