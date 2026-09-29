from django.core.validators import RegexValidator

SAUDI_PHONE_VALIDATOR = RegexValidator(
    regex=r'^05\d{8}$',
    message="Enter a valid Saudi phone number (e.g. 05XXXXXXXX)",
)