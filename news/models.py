from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200,
                             db_index=True,)
    slug = models.SlugField(max_length=200, unique=True)
    parent_id = models.ForeignKey('self',
                                  on_delete=models.CASCADE,
                                  related_name='parent_ids',
                                  blank=True,
                                  null=True)

    def get_absolute_url(self):
        return reverse("article_list_by_category", 
                        args=[self.slug])
    

class Article(models.Model):
    category_id = models.ForeignKey(Category,
                                    on_delete=models.CASCADE,
                                    related_name='articles')
    user_id = models.ForeignKey(User,
                                related_name='articles_created',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail',
                       args=[self.pk, self.slug])