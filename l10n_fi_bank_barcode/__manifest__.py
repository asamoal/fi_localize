# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Avoin.Systems
#    Copyright 2021 Avoin.Systems
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
    "name": "Finnish Bank Barcode",
    "version": "14.0.0.0.0",
    "license": "AGPL-3",
    "category": "Accounting",
    "description": """
Generate payment barcodes for invoices.
This module only adds the barcode on the invoice form, given that
- the company currency is EUR
- the amount is not zero
- the payment reference is set, and it's either the Finnish payment reference or the Finnish creditor payment reference
- the due date is set
- the bank account is set.

- Upgraded to support Odoo v14 changes by Data Mavens Limited
""",
    "author": "Avoin.Systems, Data Mavens Limited",
    "website": "https://wwww.datamavens.io",

    "depends": [
        "account",
    ],

    "data": [
        "views/account_move.xml"
    ]
}
