from django.core.exceptions import ValidationError


def validate_string_length(value, min=1, max=255):
    str_length = len(value)

    if min <= str_length <= max:
        pass
    else:
        raise ValidationError(message="String does not match accepted length parameters")
