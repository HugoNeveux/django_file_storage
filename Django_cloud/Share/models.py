from django.db import models
from django.contrib.auth.models import User
import random, string

class ShareLink(models.Model):
    """
    Stores a file path associated with an owner and a 16-chars randomly-generated
    string, used as link (argument to /Share/s/)
    """
    link = models.CharField(max_length=255, unique=True)
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=2000)

    def link_generation():
        chars = string.ascii_letters + string.digits
        rand = [random.choice(chars) for _ in range(16)]
        code = ''.join(rand)
        if ShareLink.objects.filter(link=code).exists():
            return self.link_generation(nb_chars)
        return code
