# -*- coding: utf-8 -*-
{
    'name': "Product price 1",

    'summary': """
        agregar un nuevo campo para precio 2 en el form del producto
        """,

    'description': """
       agregar un nuevo campo para precio 2
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        "views/product_view.xml",
    ],

}
