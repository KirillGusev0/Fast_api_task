# -*- coding: utf-8 -*-
from contextlib import contextmanager


@contextmanager
def Store():#db_name
    print("Store connection opened")
    try:
        #db = open(db_name, 'r')
        
        yield None#db 
    
    finally:
        print("Store connection closed")
        #db.close()  