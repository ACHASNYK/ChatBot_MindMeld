# -*- coding: utf-8 -*-
"""This module contains a template MindMeld app configuration"""

# The namespace of the application. Used to prevent collisions in supporting services across
# applications. If not set here, the app's enclosing directory name is used.
# APP_NAMESPACE = 'app-name'

# Dictionaries for the various NLP classifier configurations

# An example decision tree model for intent classification

DOMAIN_CLASSIFIER_CONFIG = {
    'model_type': 'text',
    'model_settings': {
        'classifier_type': 'logreg',
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 10,
        'grid': {
            'fit_intercept': [True, False],
            'C': [10, 100, 1000, 10000, 100000]
        },
    },
    'features': {
        'bag-of-words': {
            'lengths': [1],
        },
        'freq': {
            'bins': 5
        },
        'in-gaz': {},
        'exact': {},
        'enable-stemming': True
    }
}

INTENT_CLASSIFIER_CONFIG = {
    'model_type': 'text',
    'model_settings': {
        'classifier_type': 'logreg'
    },
    'param_selection': {
        'type': 'k-fold',
        'k': 10,
        'grid': {
            'fit_intercept': [True, False],
            'C': [0.01, 1, 100, 10000, 1000000],
            'class_bias': [1, 0.7, 0.3, 0]
        }
    },
    'features': {
        'bag-of-words': {
            'lengths': [1]
        },
        'in-gaz': {},
        'freq': {
            'bins': 5
        },
        'exact': {},
        'length': {},
        'enable-stemming': True
    }
}


#INTENT_CLASSIFIER_CONFIG = {
#    'model_type': 'text',
#    'model_settings': {
#        'classifier_type': 'dtree'
#    },
#    'param_selection': {
#        'type': 'k-fold',
#        'k': 10,
#        'grid': {
#            'max_features': ['log2', 'sqrt', 0.01, 0.1]
#        },
#    },
#    "features": {
#        "exact": {},
#    }
#}

"""
# Fill in the other model configurations if necessary
# DOMAIN_CLASSIFIER_CONFIG = {}
# ENTITY_RECOGNIZER_CONFIG = {}
# ROLE_CLASSIFIER_CONFIG = {}
"""

# A example configuration for the parser
"""
# *** Note: these are place holder entity types ***
#PARSER_CONFIG = {
#    'grandparent': {
#        'parent': {},
#        'child': {'max_instances': 1}
#    },
#    'parent': {
#        'child': {'max_instances': 1}
#    }
#}
"""
