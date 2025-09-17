import re

from detect_secrets.plugins.base import RegexBasedDetector


class DessertDetector(RegexBasedDetector):
    """Scans for tasty desserts."""
    secret_type = 'Tasty Dessert'
    denylist = (
        re.compile(
            r"(reese's peanut butter chocolate cake cheesecake|sweet potato casserole)",
            re.IGNORECASE,
        ),
    )

class VaultTokenDetector(RegexBasedDetector):
    """Scans for Vault tokens."""

    secret_type = "Vault Token"

    denylist = [
        # Service token: hvs.<string>
        re.compile(r'hvs\.[A-Za-z0-9\-_]{20,50}(?!\w)'),

        # Batch token: hvb.<string>
        re.compile(r'hvb\.[A-Za-z0-9\-_]{20,50}(?!\w)'),

        # Recovery token: hvb.<string>
        re.compile(r'hvr\.[A-Za-z0-9\-_]{20,50}(?!\w)'),
    ]
