# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Taxi",
			"color": "grey",
			"icon": "octicon octicon-location",
			"type": "module",
			"label": _("Taxi")
		}
	]