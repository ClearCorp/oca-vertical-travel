# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Travel',
    'version': '8.0.1.0.0',
    'author': "Savoir-faire Linux,Odoo Community Association (OCA)",
    'maintainer': 'Savoir-faire Linux',
    'website': 'http://www.savoirfairelinux.com',
    'license': 'AGPL-3',
    'category': 'Customer Relationship Management',
    'summary': 'Travel Management',
    'description': """
Travel
======

Travel management with passengers.

Contributors
------------
* Sandy Carter (sandy.carter@savoirfairelinux.com)
""",
    'depends': [
        'mail',
        'base_location',
    ],
    'external_dependencies': {},
    'data': [
        'security/travel_security.xml',
        'views/travel.xml',
        'views/travel_passenger.xml',
        'views/res_config.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/travel.xml',
    ],
    'test': [],
    'installable': False,
}
