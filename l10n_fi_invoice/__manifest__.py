# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) Avoin.Systems 2020

# noinspection PyStatementEffect
{
    "name": "Finnish Invoice",
    "version": "14.0.0.0.0",
    "author": "Avoin.Systems, Data Mavens Limited",
    "category": "Localization",
    "website": "https://wwww.datamavens.io",
    "license": "AGPL-3",
    "images": ["static/description/icon.png"],
    "depends": [
        "l10n_fi_invoice_delivery_date",
        "l10n_fi_bank_barcode",
    ],
    "data": [
        "views/account_move_templates.xml",
        "data/report_paperformat_data.xml",  # Only after the template
    ],
    "summary": "Suomalainen laskupohja - Updated for Odoo v14",
    "active": False,
    "installable": True,
    "auto_install": False,
    "application": False
}
