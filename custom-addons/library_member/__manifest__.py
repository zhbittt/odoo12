{
    'name': 'Library Member',
    'description': '继承library book.',
    'author': 'minwen create',
    'depends': ['library_app'],
    'application': False,
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/member_view.xml',

    ]
}