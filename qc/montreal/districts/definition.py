#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Ahuntsic-Cartierville districts',
    domain=u'Ahuntsic-Cartierville, Montréal, QC',
    file='Ahuntsic-Cartierville.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:ahuntsic-cartierville'},
)

boundaries.register(u'Anjou districts',
    domain=u'Anjou, Montréal, QC',
    file='Anjou.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:anjou'},
)

boundaries.register(u'Côte-des-Neiges—Notre-Dame-de-Grâce districts',
    domain=u'Côte-des-Neiges—Notre-Dame-de-Grâce, Montréal, QC',
    file='CDN-NDG.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:côte-des-neiges-notre-dame-de-grâce'},
)

boundaries.register(u'Lachine districts',
    domain=u'Lachine, Montréal, QC',
    file='Lachine.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:lachine'},
)

boundaries.register(u'LaSalle districts',
    domain=u'LaSalle, Montréal, QC',
    file='LaSalle.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:lasalle'},
)

boundaries.register(u'Le Plateau-Mont-Royal districts',
    domain=u'Le Plateau-Mont-Royal, Montréal, QC',
    file='Plateau-Mont-Royal.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:le_plateau-mont-royal'},
)

boundaries.register(u'Le Sud-Ouest districts',
    domain=u'Le Sud-Ouest, Montréal, QC',
    file='Le-Sud-Ouest.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:le_sud-ouest'},
)

boundaries.register(u'L\'Île-Bizard—Sainte-Geneviève districts',
    domain=u'L\'Île-Bizard—Sainte-Geneviève, Montréal, QC',
    file='LIle-Bizard-Sainte-Genevieve.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:l~île-bizard-sainte-geneviève'},
)

boundaries.register(u'Mercier—Hochelaga-Maisonneuve districts',
    domain=u'Mercier—Hochelaga-Maisonneuve, Montréal, QC',
    file='Mercier-Hochelaga-Masoinneuve.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:mercier-hochelaga-maisonneuve'},
)

boundaries.register(u'Montréal-Nord districts',
    domain=u'Montréal-Nord, Montréal, QC',
    file='Montreal-Nord.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:montréal-nord'},
)

boundaries.register(u'Outremont districts',
    domain=u'Outremont, Montréal, QC',
    file='Outremont.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:outremont'},
)

boundaries.register(u'Pierrefonds-Roxboro districts',
    domain=u'Pierrefonds-Roxboro, Montréal, QC',
    file='Pierrefonds-Roxboro.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:pierrefonds-roxboro'},
)

boundaries.register(u'Rivière-des-Prairies—Pointe-aux-Trembles districts',
    domain=u'Rivière-des-Prairies—Pointe-aux-Trembles, Montréal, QC',
    file='Riviere-des-Prairies-Pointe-aux-Trembles.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:rivière-des-prairies-pointe-aux-trembles'},
)

boundaries.register(u'Rosemont—La Petite-Patrie districts',
    domain=u'Rosemont—La Petite-Patrie, Montréal, QC',
    file='Rosemont-La-Petite-Patrie.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:rosemont-la_petite-patrie'},
)

boundaries.register(u'Saint-Laurent districts',
    domain=u'Saint-Laurent, Montréal, QC',
    file='Saint-Laurent.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:saint-laurent'},
)

boundaries.register(u'Saint-Léonard districts',
    domain=u'Saint-Léonard, Montréal, QC',
    file='Saint-Leonard.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:saint-léonard'},
)

boundaries.register(u'Verdun districts',
    domain=u'Verdun, Montréal, QC',
    file='Verdun.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:verdun'},
)

boundaries.register(u'Ville-Marie districts',
    domain=u'Ville-Marie, Montréal, QC',
    file='Ville-Marie.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:ville-marie'},
)

boundaries.register(u'Villeray—Saint-Michel—Parc-Extension districts',
    domain=u'Villeray—Saint-Michel—Parc-Extension, Montréal, QC',
    file='Villeray-St-Michel-Parc-Ex.shp',
    last_updated=date(2013, 4, 2),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/arrondissement:villeray-saint-michel-parc-extension'},
)
