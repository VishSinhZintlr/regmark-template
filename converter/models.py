from djongo import models
from uuid import uuid4
from django_enumfield import enum
from django.utils.timezone import now

class DataCell(models.Model):
    
    class Meta:
        db_table = "dataCell"
    
    class DATA_TYPE(enum.Enum):
        STRING = 1
        NUMBER = 2
        DOCUMENT = 3
        DATE_TIME = 4
        DATE = 5
        TIME = 6    
    
    class SPECIAL_TYPE(enum.Enum):
        PROJECT_COSTING_CURRENT = 1
        PROJECT_COSTING_TARGET = 2
        PROJECT_TIMELINE_CURRENT = 3
        PROJECT_TIMELINE_TARGET = 4
        OTHER = 5
    
    class CHOICE(enum.Enum):
        TRUE = 1
        FALSE = 0
    
    data_cell_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product_id = models.CharField(max_length=100)
    data_sheet_id = models.CharField(max_length=100)
    table_id = models.CharField(max_length=100)
    cell_title = models.CharField(max_length=100)
    row_no = models.IntegerField()
    col_no = models.IntegerField()
    address = models.CharField(max_length=100)
    is_header = enum.EnumField(CHOICE, default=CHOICE.FALSE)
    is_highlighted = enum.EnumField(CHOICE, default=CHOICE.FALSE)
    is_locked = enum.EnumField(CHOICE, default=CHOICE.FALSE)
    is_formula = enum.EnumField(CHOICE, default=CHOICE.FALSE)
    is_merged = models.CharField(max_length=2000, null=True, blank=True)
    formula = models.CharField(max_length=2000, null=True, blank=True)
    value = models.CharField(max_length=2000)
    foreign_reference_ids = models.JSONField()  
    strict_data_type = enum.EnumField(CHOICE, default=CHOICE.TRUE)
    is_currency = enum.EnumField(CHOICE, default=CHOICE.FALSE)
    has_budget_rule = models.UUIDField(null=True, blank=True)
    allowed_additional_budget = models.FloatField(null=True, blank=True)
    special_type = enum.EnumField(SPECIAL_TYPE, default=SPECIAL_TYPE.OTHER)
    custom_obj = models.JSONField(default={})
    data_type = enum.EnumField(DATA_TYPE, default=DATA_TYPE.STRING)
    is_being_edited = models.CharField(max_length=100, null=True, blank=True)
    is_being_edited_time_stamp = models.DateTimeField(default=now)
    create_datetime = models.DateTimeField(default=now)
    modify_datetime = models.DateTimeField(default=now)
