from collections import OrderedDict


"""Filters defined below

scope_filter(<scope>) --> dynamic scope filter
ws_scopes
store_scopes
"""


DEFAULT = 'DEFAULT'
WEBSITE = 'WEBSITE'
STORE = 'STORE'


scope_map = OrderedDict((
    ('DEFAULT', 'default'),
    ('WEBSITE International Website',  'ws_int'),
    ('WEBSITE USA Website',            'ws_us'),
    ('WEBSITE United Kingdom Website', 'ws_uk'),
    ('WEBSITE Australia Website',      'ws_au'),
    ('WEBSITE Austria Website',        'ws_at'),
    ('WEBSITE Belgium Website',        'ws_be'),
    ('WEBSITE Canada Website',         'ws_ca'),
    ('WEBSITE Denmark Website',        'ws_dk'),
    ('WEBSITE Finland Website',        'ws_fi'),
    ('WEBSITE French Website',         'ws_fr'),
    ('WEBSITE Germany Website',        'ws_de'),
    ('WEBSITE Hong Kong Website',      'ws_hk'),
    ('WEBSITE Hungary Website',        'ws_hu'),
    ('WEBSITE Indian Website',         'ws_in'),
    ('WEBSITE Ireland Website',        'ws_ie'),
    ('WEBSITE Italy Website',          'ws_it'),
    ('WEBSITE Japan Website',          'ws_jp'),
    ('WEBSITE Mexico Website',         'ws_mx'),
    ('WEBSITE Netherlands Website',    'ws_nl'),
    ('WEBSITE New Zealand Website',    'ws_nz'),
    ('WEBSITE Norway Website',         'ws_no'),
    ('WEBSITE Portugal Website',       'ws_pt'),
    ('WEBSITE Russia Website',         'ws_ru'),
    ('WEBSITE SouthAfrica Website',    'ws_sa'),
    ('WEBSITE Spain Website',          'ws_es'),
    ('WEBSITE Sweden Website',         'ws_se'),
    ('WEBSITE Switzerland Website',    'ws_ch'),
    ('STORE International-EN', 'en-int'),
    ('STORE English-US',       'en-US'),
    ('STORE English-UK',       'en-UK'),
    ('STORE English-AU',       'en-AU'),
    ('STORE English-BE',       'en-BE'),
    ('STORE English-CA',       'en-CA'),
    ('STORE English-DK',       'en-DK'),
    ('STORE English-FI',       'en-FI'),
    ('STORE English-HK',       'en-HK'),
    ('STORE English-HU',       'en-HU'),
    ('STORE English-IE',       'en-IE'),
    ('STORE English-IN',       'en-IN'),
    ('STORE English-IT',       'en-IT'),
    ('STORE English-JP',       'en-JP'),
    ('STORE English-NL',       'en-NL'),
    ('STORE English -NO',      'en-NO'),
    ('STORE English-NZ',       'en-NZ'),
    ('STORE English-SE',       'en-SE'),
    ('STORE English-ZA',       'en-ZA'),
    ('STORE French-BE',        'fr-BE'),
    ('STORE French-CA',        'fr-CA'),
    ('STORE French-CH',        'fr-CH'),
    ('STORE French-FR',        'fr-FR'),
    ('STORE German-AT',        'de-AT'),
    ('STORE German-CH',        'de-CH'),
    ('STORE German-DE',        'de-DE'),
    ('STORE Italian-CH',       'it-CH'),
    ('STORE Italian-IT',       'it-IT'),
    ('STORE Japanese-JP',      'jp-JP'),
    ('STORE Portuguese-PT',    'pt-PT'),
    ('STORE Russian-RU',       'ru-RU'),
    ('STORE Spanish-ES',       'es-ES'),
    ('STORE Spanish-MX',       'es-MX'),
))

scope_filter = lambda s: [v for k, v in scope_map.items() if s in k]

ws_scopes = filter(lambda x: 'ws_' in x, scope_map.values())
store_scopes = filter(lambda x: '-' in x, scope_map.values())
