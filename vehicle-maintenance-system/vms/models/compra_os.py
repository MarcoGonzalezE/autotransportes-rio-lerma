# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models
from datetime import datetime


class orden_servicio(models.Model):
    _inherit = "purchase.order"
    origen = fields.Many2one('vms.order', string='Orden de Servicio', required=True)

class reporte_mantenimiento(models.Model):
    _name = 'reporte.mantenimiento'
    reporte = fields.Many2one('vms.report', string='Reporte')
    pedido = fields.Char("Pedido")
    fecha = fields.Char("Pedido")
    proveedor = fields.Char("Pedido")
    producto = fields.Char("Pedido")
    cantitad = fields.Float("Pedido")
    costo = fields.Float("Pedido")

    def _sql_reporte_mantenimiento(self):
        query_function = """
        SELECT 
        po.name as Pedido, 
        po.date_order as Fecha,
        rp.name as Proveedor,
        pt.name as Producto, 
        ROUND(pol.product_qty,2) as Cantidad, 
        ROUND(pol.price_subtotal,2) as Costo,
        fv.name as Vehiculo
        from purchase_order po
        inner join vms_order mo ON mo.id = po.origen
        inner join purchase_order_line pol ON pol.order_id = po.id
        inner join product_product pp ON pp.id = pol.product_id
        inner join product_template pt ON pp.product_tmpl_id = pt.id
        inner join res_partner rp ON rp.id = po.partner_id
        inner join fleet_vehicle fv ON fv.id = po.vehicle
        """
        self.env.cr.execute(query_function)


