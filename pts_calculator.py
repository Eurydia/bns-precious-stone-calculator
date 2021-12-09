from math import ceil
from configure import SETTING
from typing import Dict


class PreciousCalculator:
    """The pts has one ingredient
    which is 170 precious stones plus the crafting fee
    of 250 gold. This yield 5 pieces of pts.

    The product will have to be sold at the least
    50 gold per piece.
    
    As for the precious stone, it has 2 ingredients
    which are 5 naryu coins and 5 elemental powder
    plus the crafting cost of 0.1 gold. This yield
    one percious stone.
    
    The naryu coins can be farmed for free, 
    but it can also be bought at 0.6 gold per piece.
    If no naryu coins were farmed, the precious stone
    will cost an additional 3 gold to craft.
    
    Unfortunately, the only feastible way to obtain 
    large numbers of elemental powder is to open chests.
    The chests cost 10 gold, and can give 5 - 8 pieces 
    of elemental powder. But for the sake of simplicity, 
    let's assume that the chests give 5 piece, or one chest
    per precious stone.
    
    In the worst cases, one precious stone will cost a total of 
    3 from buying naryu coins
    +
    10 from opening one chest to get 5 elemental powder
    + 
    0.1 from the crafting fee.
    =
    13.1 gold

    
    To get pts we need,
    2227 (170 * 13.1) from precious stone
    +
    250 from the crafting fee
    = 
    2707 (541.4) gold

    This is the amount of gold we need for 5 pieces 
    of pts if we buy everything."""



    def __init__(self) -> None:
        self.setting: Dict[str, int] = None
    
    def calculate(self) -> None:
        ps_farmed = int(input('precious_stone_farmed '))
        nc_farmed = int(input('naryu_coins_farmed '))
        ep_farmed = int(input('elemental_powder_farmed '))
        ppp = int(input('market_price_per_product '))

        # Calculate how many precious stone is missing
        # and also how much it will cost to craft them.
        ps_missing = self.ps_missing(ps_farmed)
        ps_crafting_cost = self.missing_ps_crafting_cost(
            ps_missing,
            nc_farmed,
            ep_farmed
        )

        product_crafting_fee = self.setting.get("pts_crafting_fee")
        gold_invested = ps_crafting_cost + product_crafting_fee

        product_per_craft = self.setting.get("pts_per_craft")
        gold_return = ppp * product_per_craft

        marketplace_tax = self.setting.get("marketplace_tax")
        gold_return_taxed = gold_return *marketplace_tax

        net_profit = gold_return_taxed - gold_invested

        print(
f'''\
{gold_invested=}
{gold_return=}
{gold_return_taxed=}
{net_profit=}\
'''
)  

    def ps_missing(self, ps_farmed: int) -> int:
        res = self.setting.get("ps_requried_per_crafting") - ps_farmed
        return res if res >= 0 else 0

    def missing_ps_crafting_cost(self, ps_missing: int, nc_farmed: int, ep_farmed: int) -> float:
        nc_cost = self.setting.get("nc_cost")
        nc_total_cost = self.nc_to_buy(ps_missing, nc_farmed) * nc_cost 

        chest_cost = self.setting.get("ep_chest_cost")
        chest_total_cost = self.chest_to_buy(ps_missing, ep_farmed) * chest_cost
        return nc_total_cost + chest_total_cost


    def nc_to_buy(self, ps_missing: int, nc_farmed: int) -> int:
        nc_per_ps = self.setting.get("nc_per_ps")
        nc_needed = ps_missing * nc_per_ps
        nc_to_buy = nc_needed - nc_farmed
        return nc_to_buy if nc_to_buy >= 0 else 0
    
    def chest_to_buy(self, ps_missing: int, ep_farmed: int) -> int:
        ep_per_ps = self.setting.get("ep_per_ps")
        ep_needed = ps_missing * ep_per_ps
        ep_missing = ep_needed - ep_farmed

        ep_per_chest = self.setting.get("ep_per_chest")
        ep_chest_to_buy = ceil(ep_missing / ep_per_chest)
        return ep_chest_to_buy if ep_chest_to_buy >= 0 else 0


