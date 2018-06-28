from __future__ import unicode_literals
from frappe import _

def get_data():
    return[
        {
            "label": _("Quality Management"),
            "icon": "octicon octicon-star",
            "items": [
                   {
                       "type": "doctype",
                       "name": "CAPA",
                       "label": _("CAPA"),
                       "description": _("CAPA")
                   },
                   {
                       "type": "doctype",
                       "name": "Deviation",
                       "label": _("Deviation"),
                       "description": _("Deviation")
                   }
            ]
        },
        {
            "label": _("Change Management"),
            "icon": "octicon octicon-git-branch",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Request For Change",
                       "label": _("Request For Change"),
                       "description": _("Request For Change")
                   },
                   {
                       "type": "doctype",
                       "name": "Change",
                       "label": _("Change"),
                       "description": _("Change")
                   },
                   {
                       "type": "doctype",
                       "name": "Change Impact Assessment",
                       "label": _("Change Impact Assessment"),
                       "description": _("Change Impact Assessment")
                   },
                   {
                       "type": "doctype",
                       "name": "Change Order",
                       "label": _("Change Order"),
                       "description": _("Change Order")
                   } 
            ]
        },
        {
            "label": _("Document Management"),
            "icon": "octicon octicon-file",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Document",
                       "label": _("Document"),
                       "description": _("Document")
                   }
            ]
        },
        {
            "label": _("Audit Management"),
            "icon": "octicon octicon-gist-secret",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Audit Request",
                       "label": _("Audit Request"),
                       "description": _("Audit Request")
                   }
            ]
        },
        {
            "label": _("Configuration"),
            "icon": "octicon octicon-tools",
            "items": [
                   {
                       "type": "doctype",
                       "name": "Complaint category",
                       "label": _("Complaint category"),
                       "description": _("Complaint category")
                   },
                   {
                       "type": "doctype",
                       "name": "Complaint code",
                       "label": _("Complaint code"),
                       "description": _("Complaint code")
                   },            ]
        }
    ]

