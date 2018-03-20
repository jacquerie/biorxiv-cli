# -*- coding: utf-8 -*-

"""Initial configuration for this package.

Variable ``FOO`` is overridden by adding to the environment
a variable called ``BIORXIV_FOO``.
"""

from __future__ import absolute_import, division, print_function

import os


BASE_URL = os.environ.get('BIORXIV_BASE_URL', 'http://connect.biorxiv.org/')

READ_BASE_URL = os.environ.get('BIORXIV_READ_BASE_URL', BASE_URL + 'biorxiv_xml.php?subject=')

READ_CATEGORIES = os.environ.get('BIORXIV_READ_CATEGORIES', [
    'all',
    'animal_behavior_and_cognition',
    'biochemistry',
    'bioengineering',
    'bioinformatics',
    'biophysics',
    'cancer_biology',
    'cell_biology',
    'clinical_trials',
    'developmental_biology',
    'ecology',
    'epidemiology',
    'evolutionary_biology',
    'genetics',
    'genomics',
    'immunology',
    'microbiology',
    'molecular_biology',
    'neuroscience',
    'paleontology',
    'pathology',
    'pharmacology_and_toxicology',
    'physiology',
    'plant_biology',
    'scientific_communication_and_education',
    'synthetic_biology',
    'systems_biology',
    'zoology',
])
