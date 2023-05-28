from odoo import fields,model

class TestAbstactmodel(model.AbstractModel):
    _name='test.abstract'
    _discripation='HSPL'

    name=fields.char(string='Name')
    date=fields.Date(string='Date')

class TestModel(model.AbstractModel):
    _name='test.model'
    _discripation='heliconia'

    name=fields.char(string='name')
    date=fields.Date(string='Date')

