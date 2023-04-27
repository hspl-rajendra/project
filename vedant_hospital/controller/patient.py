# from odoo.http import request, route, Controller
#
# class PaitentController(Controller):
#     @route('/patient/create', type='json', auth='public', methods=['POST'])
#     def create_patient(self, **kw):
#         # Your code to create a sale order goes here
#         print(kw)
#         vals = {
#             'name': kw.get('name') or "sunil",
#             'age': kw.get('age') or "12",
#             'ref': kw.get('ref') or "121212",
#         }
#         patient = request.env['hospital.patient'].create(vals)
#         if patient:
#          return {'message': 'Sale order created successfully!'}
#              else:
#             return {'message': 'Sale order created not ctrate!'}