from django.db import models

# models.py
class Picture(models.Model):
    id = models.AutoField(primary_key=True)
    Main_Input_Img = models.ImageField(upload_to='images/')

