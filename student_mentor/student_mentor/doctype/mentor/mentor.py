# Copyright (c) 2022, SK and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class Mentor(WebsiteGenerator):
	def before_save(self):
        	self.full_name = f'{self.first_name} {self.last_name or ""}'
