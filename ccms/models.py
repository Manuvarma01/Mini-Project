from django.db import models
from django.db.models import Model

class CaseModel(Model):

    title=models.CharField(max_length=500)
    category=models.CharField(max_length=500)
    lasthearingdate = models.CharField(max_length=500,default="")
    nexthearingdate=models.CharField(max_length=500,default="")
    casestatus=models.CharField(max_length=500,default="")
    description=models.CharField(max_length=500)
    clientid=models.CharField(max_length=500)
    lawyerid=models.CharField(max_length=500)
    lawyeracceptance=models.CharField(max_length=500,default="no")
    postedon= models.DateTimeField(auto_now=True, blank=False, null=False)

    class Meta:
        db_table = "cases"

class DocumentModel(Model):

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    caseid = models.CharField(max_length=500)
    uploaddate=models.CharField(max_length=500)
    documentname =models.FileField(upload_to="documents")

    class Meta:
        db_table = "documents"

class AppointmentModel(Model):

    clientid = models.CharField(max_length=500)
    lawyerid = models.CharField(max_length=500)
    appointmentdate = models.CharField(max_length=500,default="")
    appointmenttime = models.CharField(max_length=500,default="")
    description= models.CharField(max_length=500)

    class Meta:
        db_table = "appointments"

class LawyerModel(Model):

    name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    experience=models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    qualification = models.CharField(max_length=500)
    status=models.CharField(max_length=500,default="no")

    class Meta:
        db_table = "lawyers"


class ClientModel(Model):

    name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
    age = models.CharField(max_length=500)

    class Meta:
        db_table = "clients"