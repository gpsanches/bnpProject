# -*- coding: utf-8 -*-

from datetime import datetime


def format_date(date_str, _ret_format, current_date_format='%d %B %Y'):
    date_clean = date_str.replace("st", "").replace("nd", "").replace("rd", "").replace("th", "")
    if _ret_format == 'timestamp':
        return datetime.strptime(date_clean, current_date_format).timestamp()
    return datetime.strptime(date_clean, current_date_format).strftime(_ret_format)


def validate(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
