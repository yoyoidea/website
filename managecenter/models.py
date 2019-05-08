from django.db import models
# Create your models here.


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    describe = models.TextField(null=True, blank=True, verbose_name='描述')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    objects = BaseManager()

    class Meta:
        abstract = True


class WebSiteType(BaseModel):
    """网址类型"""
    name = models.CharField(max_length=250)
    icon = models.CharField(max_length=100)
    rank = models.IntegerField(default=0)

    class Meta:
        db_table = 'website-type'
        ordering = ['rank']

    def __str__(self):
        return self.name


class WebSite(BaseModel):
    """网址"""
    title = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey(WebSiteType, on_delete=models.CASCADE)
    url = models.CharField(max_length=250)
    logo_url = models.ImageField(
        null=True,
        blank=True,
        upload_to='image',
        max_length=200)

    class Meta:
        db_table = 'web-site'
        ordering = ['-created_time']

    def __str__(self):
        return self.title
