#RiverStation admin.py
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from RiverInspect.models import RiverInspectModel


# Register your models here.
@admin.register(RiverInspectModel)

class RiverInspectAdmin(ImportExportModelAdmin):
    list_display = ('riverName','stationName','riverstationNumber','riverStandard','inspectDate','inspectTime',
    'inspectAirTemp','inspectCMS','inspectWaterTemp','inspectPH','inspectO2','inspectTN','inspectTP','inspectBOD',
    'inspectCOD','inspectSS','inspectCd','inspectPb','inspectCr','inspectNi','inspectCu','inspectZn','inspectMn',
    'inspectEle','inspectCFU','inspectAnionic','inspectN2','inpectOrgC','inspectPers','inspectOil','inspectNTU',
    'inspectNO3N','inspectNO2N','inspectComment')


# Register your models here.
