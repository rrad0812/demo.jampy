from django.core.checks.messages import Debug
from django.db import models
from django.db.models import indexes
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, DecimalField, IntegerField
from django.db.models.fields.related import ForeignKey
from django.db.models.indexes import Index


class Artist(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=160, db_index=True)
    artist = models.ForeignKey("Artist", on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=40, db_index=True)
    last_name = models.CharField(max_length=20, db_index=True)
    title = models.CharField(max_length=30, default='')
    reports_to = models.ForeignKey("Employee", on_delete=PROTECT, null=True)
    birth_date = models.DateTimeField(null=True)
    hire_date = models.DateTimeField(null=True)
    address = models.CharField(max_length=70, default='')
    city = models.CharField(max_length=40, default='')
    state = models.CharField(max_length=40, default='')
    country = models.CharField(max_length=40, default='')
    postal_code = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=24, default='')
    fax = models.CharField(max_length=24, default='')
    email = models.EmailField(db_index=True, default='')

    class Meta:
        verbose_name_plural = "Employees"
        indexes = [
            models.Index(fields=["first_name", "last_name"]),
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Customer(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=80, default='')
    address = models.CharField(max_length=70, default='')
    city = models.CharField(max_length=40, default='')
    state = models.CharField(max_length=40, default='')
    country = models.CharField(max_length=40, default='')
    postal_code = models.CharField(max_length=10, default='')
    phone = models.CharField(max_length=24, default='')
    fax = models.CharField(max_length=24, default='')
    email = models.EmailField(db_index=True, default='')
    support = models.ForeignKey("Employee", verbose_name='Support', on_delete=PROTECT, null=True)

    class Meta:
        verbose_name_plural = "Customers"
        indexes = [
            models.Index(fields=["first_name", "last_name"])
        ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Genre(models.Model):
    name = CharField(max_length=120, db_index=True)

    class Meta:
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class MediaType(models.Model):
    name = CharField(max_length=20, db_index=True)

    class Meta:
        verbose_name_plural = "Media Types"

    def __str__(self):
        return self.name


class Track(models.Model):
    name = CharField(max_length=200)
    album = ForeignKey("Album", on_delete=PROTECT, null=True)
    media_type = ForeignKey("MediaType", on_delete=PROTECT, default=0)
    genre = ForeignKey("Genre", on_delete=PROTECT, null=True)
    composer = CharField(max_length=220, db_index=True, null=True)
    msec = IntegerField(default=0)
    bytes = IntegerField()
    unit_price = DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = "Tracks"

    def __str__(self):
        return self.name


class Invoice(models.Model):
    customer = ForeignKey("Customer", on_delete=PROTECT)
    invoice_date = DateTimeField(db_index=True)
    billing_address = CharField(max_length=70, default='')
    billing_city = CharField(max_length=40, default='')
    billing_state = CharField(max_length=40, default='')
    billing_country = CharField(max_length=40, default='')
    billing_postal_code = CharField(max_length=10, default='')
    total = DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name_plural = "Invoices"

    def __str__(self):
        return self.customer.first_name + ' ' + self.customer.last_name + ' ' + str(self.invoice_date)


class InvoiceLine(models.Model):
    invoice = ForeignKey("Invoice", on_delete=PROTECT)
    track = ForeignKey("Track", on_delete=PROTECT)
    unit_price = DecimalField(max_digits=12, decimal_places=2)
    quantity = IntegerField()

    def __str__(self):
        return self.invoice.customer.first_name + ' ' + self.invoice.customer.last_name + ' ' + str(
            self.invoice.invoice_date) + ' ' + self.track.name
