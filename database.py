from fastapi import FastAPI,Depends
from pydantic import BaseModel
from typing import Dict 

class Item(BaseModel):
    name : str 
    age :int 
    cart_id :int 

fake_db:Dict[int,Item] ={}

def get_db() -> Dict[int,Item]:
    return fake_db