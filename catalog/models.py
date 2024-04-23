from django.db import models
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField( verbose_name="Name", max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"


    def get_absolute_url(self):
        return reverse("catalog:detail", kwargs={"catalog_slug": self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"



class Tour(models.Model):
    name = models.CharField(max_length=200, verbose_name="Tour name")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tours")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    destination = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="tours")
    city = models.CharField(verbose_name="City", max_length=50, null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    duration = models.IntegerField(verbose_name="Duration", null=True, blank=True)
    is_family = models.BooleanField(verbose_name="Family", null=True, blank=True, default=False)
    is_visa = models.BooleanField(verbose_name="Visa", null=True, blank=True)
    image = models.ImageField(
        verbose_name="Image",
        upload_to="products/%Y/%m/%d",
        blank=True,
        default="default_trip.png"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)


    def __str__(self):
        return f"{self.pk} - {self.name}"

    def get_absolute_url(self):
        return reverse("catalog:tour_detail", kwargs={"tour_slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 400:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"
        ordering = ["name"]


class TourPhotos(models.Model):
    image = models.ImageField("Image", upload_to="movies/screenshots")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="tour_photos", null=True, blank=True)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    class Meta:
        verbose_name = "Screenshot"
        verbose_name_plural = "Screenshots"