from django.contrib import admin

from ccms.models import CaseModel, LawyerModel, ClientModel, DocumentModel, AppointmentModel

admin.site.register(CaseModel)
admin.site.register(LawyerModel)
admin.site.register(ClientModel)
admin.site.register(DocumentModel)
admin.site.register(AppointmentModel)
