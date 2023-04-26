from odoo.http import request, route, Controller

class PaitentController(Controller):
    @route('/api/patient/create', type='json', auth='public', methods=['POST'])
    def create_sale_order(self, **kw):
        # Your code to create a sale order goes here
        vals = {
            'name': kw.get('name') or "sunil",
            'age': kw.get('age'),
            'ref': kw.get('ref'),
        }
        patient = request.env['hospital.patient'].create(vals)
        if patient:
            return {'message': 'Sale order created successfully!'}
        else:
            return {'message': 'Sale order created not ctrate!'}