# - coding: utf-8 -*-

{

    'name': 'Booker',

    'version': '1.0.0',

    'category': '',

    'summary': 'libros ',

    'author': 'BLUEORANGE GROUP S.R.L',

    'website': 'http://www.blueorange.com.ar',

    'license': 'OPL-1',

    'depends': [

        "base",
        "mail",
    ],
    'data': [    
        'data/library_mail_template.xml',    
        'wizard/wizard_update.xml',
        'views/library_book.xml',
        'views/library_ejemplar.xml',
        'views/rules.xml',
        'views/rules_categories.xml', 
        'security/ir.model.access.csv',
    ],
    'installable': True,

    'auto_install': False,

    'application': True,

    'description': "Guardar informacion de libros",
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
