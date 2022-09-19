from django.db import models

# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    title = models.CharField(max_length=128, blank=True)
    company = models.CharField(max_length=128, blank=True)
    phone_office = PhoneNumberField(max_length=128, blank=True)
    phone_cell = PhoneNumberField(max_length=128, blank=True)
    phone_direct = PhoneNumberField(max_length=128, blank=True)
    fax = PhoneNumberField(max_length=128, blank=True)
    email = models.CharField(max_length=128, blank=True)


class Address(models.Model):
    # addresstype=models.CharField(max_length=128,blank=True)
    addressline1 = models.CharField(max_length=128, blank=True)
    addressline2 = models.CharField(max_length=128, blank=True)
    addressline3 = models.CharField(max_length=128, blank=True)
    City = models.CharField(max_length=128, blank=True)
    State = models.CharField(max_length=128, blank=True)
    Country = models.CharField(max_length=128, blank=True)
    Zipcode = models.CharField(max_length=128, blank=True)

    def _str_(self):
        return self.City


class Plant(models.Model):
    plant_location = models.CharField(max_length=128, blank=True)
    plant_contact = PhoneNumberField(max_length=128, blank=True)
    plant_address = models.ManyToManyField("Address")
    reactor = models.ManyToManyField("Reactor")

    def _str_(self):
        return self.plant_location


CHOICES_FERRULE_INSERT_IN_TUBE = (
    (True, ('yes')),
    (False, ('No'))
)
CHOICES_TUBE_PROTUDE_OUT_OF_TOP_TUBE_SHEET = (
    (True, ('yes')),
    (False, ('No'))
)
CHOICES_TUBE_PROTUDE_OUT_OF_BOTTOM_TUBE_SHEET = (
    (True, ('yes')),
    (False, ('No'))
)
CHOICES_TOP_INLET_ACCESSIBLE = (
    (True, ('yes')),
    (False, ('No'))
)
CHOICES_TOP_INLET_IMPINGMENT_PLATE = (
    (True, ('yes')),
    (False, ('No'))
)
CHOICES_TOP_DOME_REMOVABLE = (
    (True, ('yes')),
    (False, ('No'))
)


class Reactor(models.Model):
    reactor_name = models.CharField(max_length=128, blank=True)
    tube_id_in = models.CharField(max_length=128, blank=True)
    tube_id_mm = models.CharField(max_length=128, blank=True)
    is_there_ferrule_insert_in_tube = models.BooleanField(verbose_name=('is_there_ferrule_insert_in_tube'),
                                                          choices=CHOICES_FERRULE_INSERT_IN_TUBE, default="False")
    ferrule_length = models.CharField(max_length=128, blank=True)
    ferrule_id = models.CharField(max_length=128, blank=True)
    tube_material_of_tubes = models.CharField(max_length=128, blank=True)
    tube_material_of_raws = models.CharField(max_length=128, blank=True)
    tube_material_of_thermo = models.CharField(max_length=128, blank=True)
    tube_material_of_supports = models.CharField(max_length=128, blank=True)
    tube_material_of_plugs = models.CharField(max_length=128, blank=True)
    tube_material_of_coolent_tubes = models.CharField(max_length=128, blank=True)
    tube_spacing_in_or_pitch = models.CharField(max_length=128, blank=True)
    tube_spacing_mm_or_pitch = models.CharField(max_length=128, blank=True)
    tube_spacing_proof_document = models.FileField(upload_to='document/', blank=True, null=True)
    total_tube_length = models.CharField(max_length=128, blank=True)
    top_tube_sheet_thickness = models.CharField(max_length=128, blank=True)
    bottom_tube_sheet_thickness = models.CharField(max_length=128, blank=True)
    tube_protude_out_of_top_tube_sheet = models.BooleanField(verbose_name=('tube_protude_out_of_top_tube_sheet'),
                                                             choices=CHOICES_TUBE_PROTUDE_OUT_OF_TOP_TUBE_SHEET,
                                                             default="False")
    tube_protude_out_of_bottom_tube_sheet = models.BooleanField(verbose_name=('tube_protude_out_of_bottom_tube_sheet'),
                                                                choices=CHOICES_TUBE_PROTUDE_OUT_OF_BOTTOM_TUBE_SHEET,
                                                                default="False")
    top_dome_removable = models.BooleanField(verbose_name=('top_dome_removable'), choices=CHOICES_TOP_DOME_REMOVABLE,
                                             default="False")
    top_inlet_accessible = models.BooleanField(verbose_name=('top_inlet_accessible'),
                                               choices=CHOICES_TOP_INLET_ACCESSIBLE, default="False")
    top_inlet_impingment_plate = models.BooleanField(verbose_name=('top_inlet_impingment_plate'),
                                                     choices=CHOICES_TOP_INLET_IMPINGMENT_PLATE, default="False")
    any_projections_on_tube_sheet_describe = models.TextField(blank=True)
    tube_sheet_material = models.CharField(max_length=128, blank=True)
    dom_material = models.CharField(max_length=128, blank=True)
    reactor_tube_sheet_drawings = models.FileField(upload_to='images/', null=True, blank=True)
    reactor_elevation_view_drawings = models.FileField(upload_to='images/', null=True, blank=True)
    other_drawings = models.FileField(upload_to='images/', null=True, blank=True)

    def _str_(self):
        return self.reactor_name


class Client(models.Model):
    official_name = models.CharField(max_length=128)
    comman_name = models.CharField(max_length=128, blank=True)
    alternate_name = models.CharField(max_length=128, blank=True)
    key_contact = PhoneNumberField(max_length=128, blank=True)
    parent_company = models.CharField(max_length=128, blank=True)
    chemical = models.CharField(max_length=128, blank=True)
    chemical_unit = models.CharField(max_length=128, blank=True)
    unit_name = models.CharField(max_length=128, blank=True)
    reactor_per_each_unit = models.CharField(max_length=128, blank=True)

    former_name = models.CharField(max_length=128, blank=True)
    official_address = models.OneToOneField("Address", related_name="official_address", on_delete=models.DO_NOTHING)
    shipping_address = models.OneToOneField("Address", related_name="shipping_address", on_delete=models.DO_NOTHING)
    plantentrance_address = models.OneToOneField("Address", related_name="plantentrance_address",
                                                 on_delete=models.DO_NOTHING)
    plant = models.ManyToManyField("Plant")
    reactor = models.ManyToManyField("Reactor")

    def _str_(self):
        return self.official_name