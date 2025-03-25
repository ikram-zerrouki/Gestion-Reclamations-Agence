# -*- coding: utf-8 -*- 
{ 
    'name': "Gestion des réclamations", 
 
    'summary': """Gestion des réclamations pour une agence""", 
 
    'description': """ 
        Gestion des réclamations module pour trois volets : 
            - Recensement des reclamations: 
            -  Traitement des reclamations      
            -  Communication avec le reclamant  
    """, 
 
    'author': "AlMiyah Djazair", 
    'website': "http://www.AlMiyahDjazair.com", 
 
    # Categories can be used to filter modules in modules listing 
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml 
    # for the full list 
    'category': 'Test', 
    'version': '0.1', 
 
    # any module necessary for this one to work correctly 
    'depends': ['base', 'web'],  



    # always loaded 
    'data': [ 
        'security/security.xml', 
        'security/ir.model.access.csv', 
        'views/Djazair.xml', 
        'templates.xml', 
        'reports.xml', 
        
    ], 
 
    # only loaded in demonstration mode 
    'demo': [ 
        'demo.xml', 
    ], 
    
    
    'assets': {
    'web.assets_backend': [
        'static/confirm_discard.js',
    ],
},
} 