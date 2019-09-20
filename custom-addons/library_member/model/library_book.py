from odoo import fields, models


class Book(models.Model):
    _inherit = 'library.book'
    name = fields.Char('Book_Title', required=True)
    is_available = fields.Boolean('Is Availabel')
    publisher_id = fields.Many2one(index=True)
    isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")
