from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Set
from datetime import date 



@dataclass(frozen=True)
class OrderLine:
    orderid = str
    sku = str
    qty = int

class Batch:
    def __init__(self,ref:str, sku:str, qty:int, eta:Optional[date] ) -> None:
        self.ref = ref
        self.sku = sku
        self.available_quantity = qty
        self.eta = eta 

    def allocate(self,line:OrderLine):
        self.available_quantity -= line.qty 

