from django.forms import Form, CharField, PasswordInput, FileField

class LoginForm(Form):

    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())
    type=CharField(max_length=100)

class CaseForm(Form):

    title=CharField(max_length=500)
    category=CharField(max_length=500)
    description=CharField(max_length=500)
    lawyerid=CharField(max_length=500)

class DocumentForm(Form):

    title = CharField(max_length=500)
    description = CharField(max_length=500)
    caseid = CharField(max_length=500)
    documentname=FileField()

class AppointmentForm(Form):

    clientid = CharField(max_length=500)
    lawyerid = CharField(max_length=500)
    appointmentdate = CharField(max_length=500)
    appointmenttime = CharField(max_length=500)
    description= CharField(max_length=500)

class LawyerForm(Form):

    name = CharField(max_length=500)
    username = CharField(max_length=500)
    password = CharField(max_length=500)
    email = CharField(max_length=500)
    mobile = CharField(max_length=500)
    address = CharField(max_length=500)
    experience=CharField(max_length=500)
    type = CharField(max_length=500)
    qualification = CharField(max_length=500)

class ClientForm(Form):

    name = CharField(max_length=500)
    username = CharField(max_length=500)
    password = CharField(max_length=500)
    email = CharField(max_length=500)
    mobile = CharField(max_length=500)
    address = CharField(max_length=500)
    gender = CharField(max_length=500)
    age = CharField(max_length=500)