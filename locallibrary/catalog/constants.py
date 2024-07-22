from django.utils.translation import gettext_lazy as _
from enum import Enum

# Loan status
class LoanStatus(Enum):
    MAINTENANCE = "m"
    ON_LOAN = "o"
    AVAILABLE = "a"
    RESERVED = "r"

    @classmethod
    def options(cls):
        return [(key.value, _(key.name.capitalize())) for key in cls]
