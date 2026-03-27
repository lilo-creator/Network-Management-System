from django.db import models

class DisconnectLog(models.Model):
    admin_username = models.CharField(max_length=100)
    user_ip = models.GenericIPAddressField()
    user_mac = models.CharField(max_length=17)
    user_hostname = models.CharField(max_length=100, blank=True)
    disconnected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin_username} disconnected {self.user_ip} at {self.disconnected_at}"

    class Meta:
        ordering = ['-disconnected_at']