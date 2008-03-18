from django.db import models
from django.contrib.auth.models import User

class Newspost(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return "%s on %s: %s" % (self.user.first_name, self.date, self.title)

    class Admin:
        pass

    class Meta:
        ordering = ['-date']

class HotelInfo(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.PhoneNumberField()
    rate = models.DecimalField(max_digits=5,decimal_places=2)
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=15)
    zip = models.CharField(max_length=5)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Admin:
        pass

    class Meta:
        ordering = ['rate']
        verbose_name_plural = "hotel info"

class RegistrationInfo(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Admin:
        pass

    class Meta:
        verbose_name_plural = "registration info"

class Info(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url_tag = models.CharField(blank=True, max_length=40)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Admin:
        pass

    class Meta:
        verbose_name_plural = "info"

class Comments(models.Model):
    name = models.CharField(max_length=40, verbose_name="name")
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

class RSVP(models.Model):
    name = models.CharField(max_length=40, verbose_name="name")
    will_attend = models.BooleanField(verbose_name = "will attend", default=True)
    num_guests = models.PositiveSmallIntegerField(verbose_name="total number of guests", blank=True, default=0)
    additional_guests = models.TextField(verbose_name="additional guest names",blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s +%s" % (name, num_guests)

    class Admin:
        pass

    class Meta:
        verbose_name = "RSVP"
        verbose_name_plural = "RSVPs"

