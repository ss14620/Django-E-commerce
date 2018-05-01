from django.db import models
from billing.models import BillingProfile

ADDRESS_TYPE =(
                ('billing','Billing'),
                ('shipping','Shipping'),
                )
# Create your models here.
class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    address_type =models.CharField(max_length=120,choices= ADDRESS_TYPE)
    address_line_1 = models.CharField(max_length = 120)
    address_line_2 = models.CharField(max_length = 120,null=True,blank=True)
    city = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)
    country = models.CharField(max_length=120,default = 'India')

    def __str__(self):
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{line2}\n{city},{postal}\n{country}".format(
                                                                        line1 = self.address_line_1,
                                                                        line2 = self.address_line_2,
                                                                        city =self.city,
                                                                        postal =self.postal_code,
                                                                        country =self.country)
