from datetime import datetime

from django.shortcuts import render

from ccms.forms import LawyerForm, ClientForm, LoginForm, CaseForm, DocumentForm, AppointmentForm
from ccms.models import LawyerModel, ClientModel, CaseModel, DocumentModel, AppointmentModel


def lawyerregistration(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = LawyerForm(request.POST)

        if registrationForm.is_valid():

            regModel = LawyerModel()

            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.address = registrationForm.cleaned_data["address"]
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.experience = registrationForm.cleaned_data["experience"]
            regModel.type = registrationForm.cleaned_data["type"]
            regModel.qualification = registrationForm.cleaned_data["qualification"]

            user = LawyerModel.objects.filter(username=regModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'index.html', locals())
    else:
        response = render(request, 'lawyerregistration.html', {"message": "User All Ready Exist"})

    return response

def clientregistration(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = ClientForm(request.POST)

        if registrationForm.is_valid():

            regModel = ClientModel()

            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.address = registrationForm.cleaned_data["address"]
            regModel.name = registrationForm.cleaned_data["name"]
            regModel.gender = registrationForm.cleaned_data["gender"]
            regModel.age = registrationForm.cleaned_data["age"]

            user = ClientModel.objects.filter(username=regModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'index.html', locals())
    else:
        response = render(request, 'clientregistration.html', {"message": "User All Ready Exist"})

    return response

def login(request):

    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]
            type = loginForm.cleaned_data["type"]

            if type in "admin":

                if uname == "admin" and upass == "admin":

                    request.session['username'] = "admin"
                    request.session['role'] = "admin"

                    return render(request, "lawyers.html", {"lawyers":LawyerModel.objects.all()})

            if type in "client":

                client = ClientModel.objects.filter(username=uname, password=upass).first()

                if client is not None:

                    request.session['username'] = uname
                    request.session['role'] = "client"

                    return render(request, "cases.html", {"cases": CaseModel.objects.filter(clientid=uname)})

                else:
                    response = render(request, 'index.html', {"message": "Invalid Credentials"})

            if type in "lawyer":

                user = LawyerModel.objects.filter(username=uname, password=upass,status="yes").first()

                if user is not None:

                    request.session['username'] = uname
                    request.session['role'] = "lawyer"

                    return render(request, "cases.html", {"cases": CaseModel.objects.filter(lawyerid=uname)})

                else:
                    response = render(request, 'index.html', {"message": "Invalid Credentials"})

    return response

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'index.html', {})

def getlawyers(request):
    return render(request, "lawyers.html", {"lawyers":LawyerModel.objects.all()})

def activateAccount(request):

    username = request.GET['username']
    status=request.GET['status']

    LawyerModel.objects.filter(username=username).update(status=status)
    return render(request, "lawyers.html", {"lawyers":LawyerModel.objects.all()})

#============================================================================================================================

def postCase(request):
    return render(request, "postcase.html", {"lawyer":request.GET['lawyerid']})

def postCaseAction(request):

    caseForm = CaseForm(request.POST)

    if caseForm.is_valid():

        username = request.session['username']

        title = caseForm.cleaned_data['title']
        category = caseForm.cleaned_data['category']
        description = caseForm.cleaned_data['description']
        lawyerid = caseForm.cleaned_data['lawyerid']
        postedon = datetime.now()

        CaseModel(title=title,category=category,description=description,clientid=username,lawyerid=lawyerid,postedon=postedon).save()

        return render(request, "cases.html", {"cases": CaseModel.objects.filter(clientid=username)})

    else:
        return render(request, 'postcase.html', {"message": "Case Upload Failed"})

def getcases(request):

    uname=request.session['username']
    role=request.session['role']

    if role=="client":
        return render(request, "cases.html", {"cases": CaseModel.objects.filter(clientid=uname)})

    elif role=="lawyer":
        return render(request, "cases.html", {"cases": CaseModel.objects.filter(lawyerid=uname)})

    elif role == "admin":
        return render(request, "cases.html", {"cases": CaseModel.objects.all()})

def deleteCase(request):

    case_id= request.GET['caseid']
    CaseModel.objects.filter(id=case_id).delete()

    uname = request.session['username']
    role = request.session['role']

    if role == "client":
        return render(request, "cases.html", {"cases": CaseModel.objects.filter(clientid=uname)})

    elif role == "lawyer":
        return render(request, "cases.html", {"cases": CaseModel.objects.filter(lawyerid=uname)})

    elif role == "admin":
        return render(request, "cases.html", {"cases": CaseModel.objects.all()})

def updatecase(request):
    case_id = request.GET['caseid']
    return render(request, 'updatecase.html', {'case': CaseModel.objects.get(id=case_id)})

def updatecaseaction(request):

    uname = request.session['username']

    role=request.session['role']

    if role=="lawyer":

        case_id = request.GET['caseid']
        description=request.GET['description']

        CaseModel.objects.filter(id=case_id).update(description=description)

        return render(request, "cases.html", {"cases": CaseModel.objects.filter(lawyerid=uname)})

    elif role=="admin":

        case_id = request.GET['caseid']

        status = request.GET['casestatus']
        lasthearingdate = request.GET['lasthearingdate']
        nexthearingdate = request.GET['nexthearingdate']

        CaseModel.objects.filter(id=case_id).update(casestatus=status, lasthearingdate=lasthearingdate,
                                                    nexthearingdate=nexthearingdate)

        return render(request, 'cases.html', {'cases': CaseModel.objects.all()})

def acceptorrejectcase(request):

    caseid = request.GET['caseid']
    lawyerstatus=request.GET['lawyerstatus']

    CaseModel.objects.filter(id=caseid).update(lawyeracceptance=lawyerstatus)

    return render(request, "cases.html", {"cases": CaseModel.objects.filter(lawyerid=request.session['username'])})

#====================================================================================
def uploaddocument(request):
    return render(request, 'uploaddocument.html', {'caseid':request.GET['caseid']})

def uploaddocumentaction(request):

    postForm = DocumentForm(request.POST, request.FILES)

    if postForm.is_valid():

        title = postForm.cleaned_data['title']
        description = postForm.cleaned_data['description']
        caseid = postForm.cleaned_data['caseid']
        documentname = postForm.cleaned_data['documentname']
        uploaddate=datetime.now()

        DocumentModel(title=title,documentname=documentname,description=description,caseid=caseid,uploaddate=uploaddate).save()

        documents = []

        for document in DocumentModel.objects.filter(caseid=caseid):
            document.documentname = str(document.documentname).split("/")[1]
            documents.append(document)

        return render(request, "documents.html", {"documents": documents})

    else:
        return render(request, "cases.html", {"cases": CaseModel.objects.filter(lawyerid=request.session['username']),"message":"document upload failed"})

def getdocuments(request):

    documents = []

    for document in DocumentModel.objects.filter(caseid=request.GET['caseid']):
        document.documentname = str(document.documentname).split("/")[1]
        documents.append(document)

    return render(request, "documents.html", {"documents":documents})

def deletedocuments(request):

    caseid=request.GET['caseid']

    DocumentModel.objects.get(id=caseid).delete()

    documents=[]

    for document in DocumentModel.objects.filter(caseid=caseid):
        document.documentname= str(document.documentname).split("/")[1]
        documents.append(document)

    return render(request, "documents.html", {"documents":documents})

#===========================================================================================================================
def postAppointment(request):
    return render(request, "postappointment.html", {"lawyerid":request.GET['lawyerid']})

def postAppointmentAction(request):

    clientid = request.session['username']
    lawyerid = request.GET['lawyerid']
    description = request.GET['description']

    AppointmentModel(clientid=clientid,lawyerid=lawyerid,description=description).save()

    return render(request, "appointments.html",{"appointments": AppointmentModel.objects.filter(clientid=clientid)})

def getappointments(request):

    uname=request.session['username']
    role=request.session['role']

    if role=="client":
        return render(request, "appointments.html", {"appointments": AppointmentModel.objects.filter(clientid=uname)})

    elif role=="lawyer":
        return render(request, "appointments.html", {"appointments": AppointmentModel.objects.filter(lawyerid=uname)})

def deleteAppointment(request):

    appointment_id= request.GET['appointmentid']

    AppointmentModel.objects.filter(id=appointment_id).delete()

    uname = request.session['username']
    role = request.session['role']

    if role == "client":
        return render(request, "appointments.html", {"appointments": AppointmentModel.objects.filter(clientid=uname)})

    elif role == "lawyer":
        return render(request, "appointments.html", {"appointments": AppointmentModel.objects.filter(lawyerid=uname)})

def updateappointment(request):
    appointment_id = request.GET['appointmentid']
    return render(request, 'updateappointment.html', {'appointment': AppointmentModel.objects.get(id=appointment_id)})

def updateappointmentaction(request):

    uname = request.session['username']

    appointment_id = request.GET['appointmentid']

    appointmentdate=request.GET['appointmentdate']
    appointmenttime=request.GET['appointmenttime']

    AppointmentModel.objects.filter(id=appointment_id).update(appointmentdate=appointmentdate,appointmenttime=appointmenttime)

    return render(request, "appointments.html", {"appointments": AppointmentModel.objects.filter(lawyerid=uname)})

#==============================================================================================================================