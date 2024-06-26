from django.db import models

from catalog.models import Tour

ORDER_STATUS_CHOICES = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
)


class Order(models.Model):
    status = models.CharField(
        verbose_name='Status',
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default='pending'
    )
    tour = models.ManyToManyField(Tour, related_name='tour_orders', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order - {self.pk}"


    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        indexes = [
            models.Index(fields=["-created_at"])
        ]

class OrderInfo(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='info')
    first_name = models.CharField(verbose_name='First Name', max_length=50)
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    email = models.EmailField(verbose_name='Email', max_length=100)
    phone = models.CharField(verbose_name='Phone', max_length=200, blank=True)
    city = models.CharField(verbose_name='City', max_length=50, blank=True)
    members = models.PositiveIntegerField(verbose_name='Members', default=1)

    date_from = models.DateField(verbose_name='Start date', blank=True, null=True)
    date_to = models.DateField(verbose_name='End date', blank=True, null=True)

    def __str__(self):
        return f"Order info - {self.order.pk}: {self.first_name} {self.last_name}"


    class Meta:
        verbose_name = "Order information"



