from django.db import models
from .services import generate_token, generate_access_token

class Seller(models.Model):
    def generate_token_internal():
        return generate_token(7)
    
    def generate_access_tokn():
        return generate_access_token()

    name = models.CharField(max_length=50)
    comissionPercent = models.IntegerField(choices=[
    (5, 'Tercera Clase'),
    (15, 'Segunda Clase'),
    (25, 'Primera Clase'),
    ])
    token = models.CharField(max_length=50, default=generate_token_internal)
    access_tokn = models.CharField(max_length=50, default=generate_access_tokn)

    
    @property
    def total_balance(self):
        trans_acumulate = self.transact_set.aggregate(total_bal=models.Sum('total'))['total_bal'] 
        if trans_acumulate != 0 and trans_acumulate != None:
            return round(trans_acumulate * self.comissionPercent / 100, 2)
        else:
            return 0

    @property
    def total_transacts(self):
        return self.transact_set.count()
    
class Product(models.Model):
    def generate_token_internal():
        return generate_token(5)

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, default="")
    token = models.CharField(max_length=50, default=generate_token_internal)
    image= models.ImageField(upload_to='images/products', null=True)

    @property
    def product_transacts_count(self):
        return self.transact_set.count()   

class Transact(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)



