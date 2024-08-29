#!/usr/bin/env python3
from werkzeug.routing import BaseConvertor
from datetime import datetime


class DateConverter(BaseConvertor):
    '''Date converter class'''

    def to_python(self, value):
        '''Convert string to date'''
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        '''Convert date to string'''
        return value.strftime('%Y-%m-%d')
