from django.contrib import admin

# Register your models here.
#importar nossos modelos
from .models import User

admin.site.register(User)  
