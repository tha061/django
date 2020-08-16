from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django_mysql.models import ListCharField
from django.db.models import CharField



class Link(models.Model):
    link_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, default=None,blank=True, on_delete=models.PROTECT, null = True)
    firstChar = models.CharField(max_length=1, blank=True, null=True)
    fileSize = models.CharField(max_length=200, blank=True, null=True)
    VT_permallink = models.CharField(max_length=100, blank=True, null=True)
    VT_sha1 = models.CharField(max_length=100, blank=True, null=True)
    VT_responseCode = models.CharField(max_length=100, blank=True, null=True)
    VT_resource = models.CharField(max_length=100, blank=True, null=True)
    VT_scanId = models.CharField(max_length=100, blank=True, null=True)
    VT_msg = models.CharField(max_length=100, blank=True, null=True)
    VT_sha256 = models.CharField(max_length=100, blank=True, null=True)
    VT_md5 = models.CharField(max_length=100, blank=True, null=True)
    jsonFile = models.FileField(blank = True, null = True, upload_to='Static')
    certFile = models.FileField(blank = True, null = True, upload_to='Certificate')
    VTFile = models.FileField(blank = True, null = True, upload_to='VirusTotal')
    privacylink = models.CharField(max_length=200, blank=True, null=True)
    privacyText = models.CharField(max_length=10000, blank=True, null=True)
    smaliList = ListCharField(
        base_field=CharField(max_length=50),
        size=30,
        max_length=(50 * 50),  # 6 * 10 character nominals, plus commas
        blank = True,
        null = True
    )


    #rating = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.link_text
# Create your models here.
