#!/usr/bin/env python

"""mageconfifg2xlsx converts .csv files with Magento's core_config_data into Excel"""


import os
import glob
from collections import defaultdict
import unicodecsv as csv
from xlsxwriter.workbook import Workbook
import scope


scope_enum = (
    scope.DEFAULT,
    scope.WEBSITE, 
    scope.STORE
)


def get_config(current_scope, csv_dict):
    """Collect the different scopes per config key"""
    config = defaultdict(lambda: defaultdict(unicode))
    for row in csv_dict:
        if current_scope in row['scope_name']:
            for s in scope.scope_filter(current_scope):
                config[row['path']][s]
            config[row['path']][scope.scope_map[row['scope_name']]] = row['value']
    return config


def get_result(current_scope, config):
    """Transform the flat config into 2 dimensions"""
    header1 = 'Top-level'
    header2 = current_scope + ' config key'
    results = [[header1, header2] + scope.scope_filter(current_scope)]

    for path in sorted(config.keys()):
        idx = len(results) - 1
        results.append([path.split('/')[0]] + [path])
        for s in scope.scope_filter(current_scope):
            value = config[path][s]
            results[idx].append(value)
    return results


for csvfile in glob.glob(os.path.join('.', '*.csv')):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    scope_worksheets = dict()

    configs = dict()

    with open(csvfile, 'rb') as f:
    	dialect = csv.Sniffer().sniff(f.read(1024))
    	f.seek(0)
        reader = csv.DictReader(f, dialect=dialect, doublequote=False, escapechar='\\')

        for s in scope_enum:
            scope_worksheets[s] = workbook.add_worksheet(s)
            scope_worksheets[s].freeze_panes(1, 1)
            # extracting the configurations for each scope
            configs[s] = get_config(s, reader)
            f.seek(0)

    results = dict()

    for s in scope_enum:
        # get the 2-dimensional config representation
        results[s] = get_result(s, configs[s])
        
        # save to Excel sheet
        for r, row in enumerate(results[s]):
            for c, col in enumerate(row):
                scope_worksheets[s].write(r, c, col)
    
    workbook.close()
