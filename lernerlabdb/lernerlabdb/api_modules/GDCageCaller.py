
import numpy as np
import pandas as pd
import gspread

from datetime import datetime

#!TODO Type hining
#!TODO Unit testing

class GDCageCaller:
    def __init__(self):
        self.gc_oauth = gspread.oauth()
        self._key = '1rUDVrQpGKd-l1ZYN_13jH3anQS_OrtfAYaAa_wNTdMY'
        self._url = 'https://docs.google.com/spreadsheets/d/1rUDVrQpGKd-l1ZYN_13jH3anQS_OrtfAYaAa_wNTdMY/edit#gid=2099224481'
        self._sheet = None
        self._cage_data = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def sheet(self):
        return self._sheet

    @sheet.setter
    def sheet(self, sheet):
        self._sheet = sheet

    @property
    def cage_data(self):
        if self._cage_data is None:
            print('Getting Cage Data')
            self.get_cage_sheet_by_url()
        return self._cage_data

    @cage_data.setter
    def cage_data(self, cage_data):
        self._cage_data = cage_data

    def get_cage_sheet_by_url(self):
        self.sheet = self.gc_oauth.open_by_url(self.url).sheet1
        self.cage_data = pd.DataFrame(self.sheet.get_all_records())

    def clean_cage_data(self):
        cols = ['Mouse', 'CCM Barcode', 'Parent Cage',
                '# of animals', 'Sex', 'DOB', 'Location',
                'Genotype \nStrikethrough numbers when finished using\nMove to SACd cage tab when cage is done',
                'Protocol']
        df = (self.cage_data
              [cols]
              .rename(columns=lambda col: col.replace(' ', '_').lower().split('\n')[0])
              .rename({'ccm_barcode': 'barcode',
                       '#_of_animals': 'num_animals',
                       'genotype_': 'zygosity',
                       'mouse': 'cage_nickname',
                       'dob': 'date_of_birth'}, axis=1)
              .assign(
                  barcode=lambda df_: pd.to_numeric(
                      df_.barcode.str[3:], errors='coerce'),
                  sex=lambda df_: df_.sex.replace({'Male': 'M',
                                                   'Female': 'F'},
                                                  regex=True),
                  date_of_birth=lambda df_: pd.to_datetime(
                      df_.date_of_birth),
                  num_animals=lambda df_: pd.to_numeric(
                      df_.num_animals, errors='coerce')
              )
              .query('num_animals > 0')
              )

        self.cage_data = df
        return self
