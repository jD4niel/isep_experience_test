# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class PartnerExperienceReport(models.AbstractModel):
    _name = "report.isep_practice_test.experience_pdf"
    _description = "Partner Experience"

    
    @api.model
    def _get_report_values(self, docids, data=None):
        print("doc_ids: %s"%docids)
        return {
            'doc_ids': self.env['res.partner'].browse(docids),
            'doc_model': 'res.partner',
        }