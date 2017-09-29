from frappe import _

def get_data():
   return {
      'fieldname': 'change',
      'transactions': [
         {
            'label': _('Related documents'),
            'items': ['Request For Change', 'Change Impact Assessment', 'Change Order']
         }
      ]
   }
