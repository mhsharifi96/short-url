from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Links(models.Model):
    short_link = models.CharField(max_length=255,unique=True)
    main_link = models.CharField(max_length=1000)
    expire_date = models.DateTimeField(null=True,blank=True)
    note = models.CharField(max_length=500,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    count_view = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.short_link
    # def save(self, *args, **kwargs):
    #     # slugify short link
    #     self.short_link = slugify(self.short_link)
    #     super(Links, self).save(*args, **kwargs)

    class Meta:
        db_table = 'links'
        verbose_name_plural = "Links"



class Links_log(models.Model):
    src_ip = models.CharField(max_length=255,null=True,blank=True)
    dst_ip = models.CharField(max_length=255,null=True,blank=True)
    link = models.CharField(max_length=255,null=True)
    user_agent = models.CharField(max_length=255,null=True)
    cookie = models.CharField(max_length=255,null=True,blank=True)
    details = models.CharField(max_length=500,null=True,blank=True)
    meta_json = models.JSONField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        db_table = 'links_log'
        verbose_name_plural = "Links log"

class packets_log (models.Model):
    user_mac = models.CharField(max_length=255,null=True,blank=True)
    user_ip = models.CharField(max_length=255,null=True,blank=True)
    time_request = models.DurationField(default=0)
    # date_request = models.DateTimeField()
    date_request = models.CharField(max_length=255,null=True,blank=True)

    cookie = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.user_ip


    class Meta:
        db_table = 'packets_log'
        verbose_name_plural = "packets log"


# UIBvzAgDWy