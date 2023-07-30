import random
import string
import pytest
import os
import warnings

from ledgerlib.ledger.ledger import Ledger

folder_name = ''.join(random.choices(string.ascii_lowercase, k=7))

def test_check__init__():
    with pytest.warns():
        l = Ledger(folder_name)
    with warnings.catch_warnings():
        warnings.simplefilter('error')
        l = Ledger('data')
    
def test_check_if_folder_exists():
    l = Ledger(folder_name)
    assert l.check_if_folder_exists() == False
    l = Ledger('data')
    assert l.check_if_folder_exists() == True