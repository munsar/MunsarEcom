from django.db import models
from django.utils import timezone


class Shop(models.Model):

	shopName = models.CharField(max_length=100)
	shopDesc = models.CharField(max_length=200)
	shopRating = models.IntegerField()
	shopLocation = models.CharField(max_length=100)

	def __str__(self):
		return self.shopName

class Category(models.Model):
	categoryName= models.CharField(max_length=100)
	shop = models.ForeignKey(Shop, related_name="reference", on_delete=models.CASCADE)

	def __str__(self):
		return self.categoryName

class SubCategory(models.Model):
	
	category = models.ForeignKey(Category, related_name='reference', on_delete=models.CASCADE)
	subCategoryName = models.CharField(max_length=100)
	def __str__(self):
		return self.subCategoryName

class Product(models.Model):
	productSubCategory = models.ForeignKey(SubCategory, related_name="reference", on_delete=models.CASCADE)
	productName= models.CharField(max_length=100)
	productDesc = models.CharField(max_length=1500)
	productSpecs = models.CharField(max_length=1500)
	productImage = models.ImageField(upload_to='static/img')
	productImageAlt = models.CharField(max_length=150)
	productStock = models.IntegerField()
	productPrice = models.IntegerField()
	productCPrice= models.IntegerField(default=0)
	
	def __str__(self):
		return self.productName

#class ProductImage(models.Model):
#	product = models.ForeignKey(Product, related_name='reference',on_delete=models.CASCADE)
#	image = models.ImageField(upload_to='static/img')
#	title = models.CharField(max_length=50)

#	def __str__(self):
#		return self.title

class SliderImage(models.Model):
	image = models.ImageField(upload_to='store/static/slider/img')
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title



class Entry(models.Model):
	title = models.CharField(max_length=50)
	quantity = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
	sale = models.BooleanField(default=True)
	
	

	def __str__(self):
		return self.title




class CartItem(models.Model):
    product = models.ForeignKey(Product, related_name='carted', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    #user = models.ForeignKey(User, on_delete=models.CASCADE) 



#class MonthlySales(models.Model):
#	item = models.CharField(max_length=50)
#	quantity = models.IntegerField()
#	totalsale = models.IntegerField()

#	def __str__(self):
#		return self.item

#class MonthlyPurchase(models.Model):
##	item = models.CharField(max_length=50)
#	quantity = models.IntegerField()
#	totalsale = models.IntegerField()

#	def __str__(self):
#		return self.item
