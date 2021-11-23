from django.contrib import admin
from .models import Artist, Album, Employee, Customer, Genre, MediaType, Track, Invoice, InvoiceLine


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_per_page = 20


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_select_related = True  # biće join na artist model
    list_per_page = 20
    list_display = ("title", "artist",)
    search_fields = ("title", "artist__name",)  # Pretražuje po lookup polju
    autocomplete_fields = ("artist",)           # da bi izbegli prepunjavanje liste lookup-a artist


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_select_related = True
    list_per_page = 20
    list_display = ("get_name", "title", "city", "country", "email")
    search_fields = ("first_name", "last_name",)

    fields = (
        ("first_name", "last_name"),
        ("title", "reports_to",),
        ("birth_date", "hire_date",),
        ("address", "city", "state", "country", "postal_code", "phone", "fax", "email")
    )

    @admin.display(description="name", ordering="last_name")
    def get_name(self, obj):
        return obj.first_name + ' ' + obj.last_name


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_select_related = ("support",)
    list_per_page = 20
    list_display = ("get_name", "company", "city", "country", "email", "support",)
    search_fields = ("first_name", "last_name", "support__last_name")

    list_filter = ("country", "support")

    fields = (
        ("first_name", "last_name",),
        "company",
        ("address", "city", "state", "country", "postal_code", "phone", "fax", "email"),
        "support",
    )

    @admin.display(description="name", ordering="last_name")
    def get_name(self, obj):
        return obj.first_name + " " + obj.last_name


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ("name",)


@admin.register(MediaType)
class MediaTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    # list_select_related= ("genre", "media_type", "album",)
    list_per_page = 15
    list_display = ("name", "composer", "album", "genre", "get_artist", "media_type", "msec", "bytes", "unit_price")
    search_fields = ("name", "composer", "album__title", "album__artist__name")
    autocomplete_fields = ("album",)

    @admin.display(description="artist", ordering="album__artist__name")
    def get_artist(self, obj):
        return obj.album.artist.name

    fields = (
        ("name", "composer",),
        "album",
        "genre",
        ("media_type", "msec", "bytes",),
        "unit_price",
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("genre", "media_type", "album__artist", )


class InvoiceInLineAdmin(admin.TabularInline):
    model = InvoiceLine
    autocomplete_fields = ("track",)
    extra = 0

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("invoice", "invoice__customer",
                                       "track", )  # Mora i lookup lookup-a customer, inače pravi duple upite


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ("invoice_date", "customer", "total",)
    search_fields = ("invoice_date", "customer__first_name", "customer__last_name")
    autocomplete_fields = ("customer",)
    fields = (("customer", "invoice_date"), ("billing_address", "billing_postal_code", "billing_city"),
              ("billing_state", "billing_country"), "total",)
    readonly_fields = ("total",)

    inlines = [InvoiceInLineAdmin, ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("customer", )
