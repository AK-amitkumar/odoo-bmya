# -*- encoding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution	
#
#    Copyright (c) 2015 Blanco Martin y Asociados - Nelson Ram�rez S�nchez http://blancomartin.cl
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Account Money Advances", 
    "version": "1.0", 
    "author": "Blanco Martin y Asociados - Nelson Ram�rez S�nchez", 
    "category": "Generic Modules", 
    "description": """
Account Money Advances
=======================

This module lets you change the account the moment you are paying.

    """, 
    "website": "http://blancomartin.cl", 
    "license": "AGPL-3", 
    "depends": [
        "account", 
        "account_voucher"
    ], 
    "demo": [], 
    "data": [        
        "view/account_money_advances_view.xml"
    ], 
    "installable": True, 
    "auto_install": False, 
    "active": False
}