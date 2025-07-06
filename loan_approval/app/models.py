from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ApprovalModel(models.Model):
    name = models.CharField(max_length=255)
    
    EDUCATION_LVL_CHOICES = (
        ('graduate', 'Graduate'),
        ('not graduate', 'Not Graduate'),
    )
    education = models.CharField(max_length=12, choices=EDUCATION_LVL_CHOICES, default='graduate')

    EMPLOYEMENT_STATUS_CHOICES = (
        ('employed', 'Employed'),
        ('unemployed', 'Unemployed'),
    )
    emplyement_status = models.CharField(max_length=10, choices=EMPLOYEMENT_STATUS_CHOICES, default='employed')

    dependents = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

    income = models.IntegerField(
        default=200000,
        validators=[
            MinValueValidator(200000),
            MaxValueValidator(9900000)
        ]
    )

    credit_score = models.IntegerField(
        default=350,
        validators=[
            MinValueValidator(300),
            MaxValueValidator(900)
        ]
    )

    loan_amount = models.IntegerField(
        default=300000,
        validators=[
            MinValueValidator(300000),
            MaxValueValidator(39500000)
        ]
    )
    
    loan_term = models.IntegerField(
        default=2,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(20)
        ]
    )

    resident_asset = models.IntegerField(
        default=300000,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(29100000)
        ]
    )

    commercial_asset = models.IntegerField(
        default=300000,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(19400000)
        ]
    )

    luxury_asset = models.IntegerField(
        default=300000,
        validators=[
            MinValueValidator(300000),
            MaxValueValidator(39200000)
        ]
    )

    bank_asset = models.IntegerField(
        default=300000,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(14700000)
        ]
    )

    def __str__(self):
        return f"{self.name}'s Loan Approval Form"
