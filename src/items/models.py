from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files import File




class Item(models.Model):
    user         = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    activity     = models.CharField(max_length=100)
    time_created = models.DateTimeField(default=timezone.now)
    is_done      = models.BooleanField(default=False)
    time_done    = models.DateTimeField(null=True, blank=True)
    description  = models.TextField(blank=True, null=True)
    image_url    = models.CharField(max_length=200, blank=True, null=True)
    image        = models.ImageField(blank=True, null=True, upload_to='mediafiles')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        size = 600, 600
        if self.image:
            image = Image.open(self.image.path)
            image = ImageOps.exif_transpose(image)
            image.thumbnail(size, Image.LANCZOS)
            image.save(self.image.path)





'''
#6    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        size = 512, 1024
        if self.image:
            image = Image.open(self.image.path)
            image.thumbnail(size, Image.LANCZOS)
            image.save(self.image.path)



#5
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        basewidth = 1000
        img = Image.open(self.image.path)
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.Resampling.LANCZOS)
        img.save(self.image.path)

#4
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image.path)
        format = image.format
        image = ImageOps.mirror(image)
        new_size = (image.width//2, image.height//2)
        image.thumbnail(new_size, Image.ANTIALIAS)
        image.save(self.image.path, format)

#3
# this fxn is defined before the model.
def compress(image):
    
        # --- resize ---
        img = Image.open(image)
        img = img.convert("RGB")

        (w, h) = img.size   # current size (width, height)

        if w > 1000:
            new_size = (1000, 1000)  # new size
            img = img.resize(new_size, Image.ANTIALIAS)
        
        # --- convert to File ---
        im_io = BytesIO() 
        img.save(im_io, 'JPEG', quality=70) 

        new_image = File(im_io, name=image.name)

        return new_image


    def save(self, *args, **kwargs): 

        if self.image:
            # call the compress function
            new_image = compress(self.image)
            # set self.image to new_image
            self.image = new_image

        super().save(*args, **kwargs)

#2.  
    def save(self, *args, **kwargs):
        if self.image:
            new_image = self.reduce_image_size(self.image)
            self.image = new_image
        super().save(*args, **kwargs)

    def reduce_image_size(self, profile_pic):
        img = Image.open(profile_pic)
        thumb_io = BytesIO()
        img.save(thumb_io, 'jpeg', quality=50)
        new_image = File(thumb_io, name=profile_pic.name)
        return new_image


#1.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 512 or img.width > 1024:
            output_size = (int(img.width/2), int(img.height/2))
            #output_size = (1024, 512)  # width by height
            img.thumbnail(output_size)
            img.save(self.image.path)
'''
  