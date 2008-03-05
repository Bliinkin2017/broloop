from django.db import models
from django.contrib.auth.models import User

class Newspost(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(maxlength=200)
    content = models.TextField()

    def __str__(self):
        return "%s on %s: %s" % (self.user.first_name, self.date, self.title)

    class Admin:
        pass

    class Meta:
        ordering = ['-date']

class HotelInfo(models.Model):
    name = models.CharField(maxlength=40)
    phone_number = models.PhoneNumberField()
    rate = models.FloatField(max_digits=5,decimal_places=2)
    street = models.CharField(maxlength=40)
    city = models.CharField(maxlength=15)
    zip = models.CharField(maxlength=5)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Admin:
        pass

    class Meta:
        ordering = ['rate']
        verbose_name_plural = "hotel info"

class RegistrationInfo(models.Model):
    name = models.CharField(maxlength=40)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Admin:
        pass

    class Meta:
        verbose_name_plural = "registration info"

class Info(models.Model):
    title = models.CharField(maxlength=200)
    content = models.TextField()
    url_tag = models.CharField(blank=True, maxlength=40)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Admin:
        pass

    class Meta:
        verbose_name_plural = "info"

class Comments(models.Model):
    name = models.CharField(maxlength=40, verbose_name="name")
    content = models.TextField(verbose_name="comment")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s on %s" % (self.name, self.date)

    class Admin:
        pass

    class Meta:
        ordering = ['-date']
        verbose_name = "comment"
        verbose_name_plural = "comments"
