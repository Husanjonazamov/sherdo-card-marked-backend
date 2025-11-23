from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Foydalanuvchilar"),
        "separator": True, 
        "items": [
            {
                "title": _("Foydalanuvchilar"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
        ],
    },
]
