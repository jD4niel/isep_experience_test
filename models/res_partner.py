# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"
    

    experience_ids = fields.One2many('partner.experience', 'partner_id', string='Experience')
    skills_count = fields.Integer('Skill count', default=0)

    @api.onchange('experience_ids')
    def _onchange_experience_ids(self):
        args = {}
        for line in self:
            print("line.experience_ids: %s"%line.experience_ids)
            line.skills_count = len(line.experience_ids)
        return args


    @api.model
    def create(self, vals):
        res = super(ResPartner, self).create(vals)
        if res:
            self.env['partner.experience'].create({
                'partner_id': res.id,
                'skill': 'Odoo',
                'company_id': res.company_id.id,
            })
        return res

    def asign_skills(self):
        return {
            'name': 'Add Skills',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'add.skills.wizard',
            'context': {'default_partner_id': self.id,},
            'target': 'new',
        }

    def print_experience_report(self):
        docids = self.env['res.partner'].search([('active', '=', True),('skills_count','>',0)], order="skills_count desc")
        if docids:
            return self.env.ref('isep_practice_test.experience_report_print').report_action(docids=docids)

        raise UserError(u"No records found!")


class PartnerExperience(models.Model):
    _name = "partner.experience"
    _description = "Partner Experience"


    def _get_display_name(self):
        for line in self:
            name = ''
            if line.partner_id:
                name += line.partner_id.name + ' - ' 
            if line.skill:
                name += str(line.skill)
            if line.experience_percentage:
                name += ' Exp. '+str(line.experience_percentage) + '%'
            line.name = name


    name = fields.Char('Name', compute="_get_display_name", readonly=True)
    partner_id = fields.Many2one('res.partner', string='Contact')
    skill = fields.Char('Skill')
    experience_year = fields.Integer('Experience Years', default=0)
    experience_percentage = fields.Float('Experience Percentage', default=0)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)


    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        args = {}
        for line in self:
            if line.partner_id:
                line.partner_id._onchange_experience_ids()
        return args

    
    