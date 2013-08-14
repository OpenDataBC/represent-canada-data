from datetime import date

import boundaries

boundaries.register("St. John's wards",
    domain="St. John's, NL",
    last_updated=date(2012, 8, 17),
    name_func=boundaries.attr('WARDNAME'),
    id_func=boundaries.attr('WARD'),
    authority="City of St. John's",
    encoding='iso-8859-1',
    is_valid_func=lambda f: int(f.get('WARD')) != 0,
    metadata={'geographic_code': '1001519'},
)
