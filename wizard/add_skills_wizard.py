# -*- coding: utf-8 -*-
from odoo import fields, models


class AddSkillsWizard(models.TransientModel):
    _name = "add.skills.wizard"
    _description = "Add multiple skills to Partner"

    partner_id = fields.Many2one('res.partner', string='Partner')
    skill_ids = fields.Many2many('partner.experience', 'add_skills_from_wizard', 'wizard_id', 'experience_id', string='Experience')


    def action_add(self):
        if self.skill_ids:
            self.skill_ids.write(dict(partner_id=self.partner_id.id))
        