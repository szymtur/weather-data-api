import re

from django.core.validators import ValidationError, validate_email


def password_validator(password):
    if (re.search('[A-Z]', password) is None or re.search('[a-z]', password) is None or
            re.search('[0-9]', password) is None or not (8 < len(password) < 32)):

        raise ValidationError('password must be between 8 to 20 characters, '
                              'must include small and capital letters and at least one digit')


def username_validator(username):
    if not re.search('[\s\t\\\\[\\]@!#$%^&*+=()<>?/|}{~:;,`"\']', username) is None:
        raise ValidationError('username cannot contains any special characters')


def email_validator(email):
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError('invalid email address format')
