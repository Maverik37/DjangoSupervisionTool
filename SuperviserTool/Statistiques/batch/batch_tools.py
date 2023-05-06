#!/bin/env  python3
from datetime import *

def convert_byte_to_float(bytes):
    kb = float(1024)
    gb = float(kb ** 3)

    byte_converted = round(float(bytes/gb),2)
    return byte_converted

def current_date_to_string():
    o_current_date = datetime.now()
    s_date = o_current_date.strftime("%d/%m/%y %H:%M:%S")
    return s_date