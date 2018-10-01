from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    '''
    Location model
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Editor(models.Model):
    '''
    Editor model
    '''
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()
    
    def save_delete(self):
        self.delete()
    
    # def save_show_all(self):
    #     self.save.objects.all()

    class Meta:
        ordering = ['first_name']
    
class Location(models.Model):
    '''
    Location model
    '''
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
    def save_tags(self):
        self.save()

class Image(models.Model):
    '''
    Image model
    '''
    title = models.CharField(max_length =60)
    description = models.TextField()
    category = models.ManyToManyField(category)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'images/')
    location = models.ForeignKey(Location)
    
    def __str__(self):
        return self.title
    
    def save_article(self):
        self.save()
    
    def save_delete(self):
        self.delete()



    @classmethod
    def gallery_image(cls):
        images = cls.objects.all()
        
        return images
    @classmethod
    def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images

    



