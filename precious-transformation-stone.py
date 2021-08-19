from math import ceil
### BASE INFO ###
crafting_fee = 250
product_per_craft = 5

precious_stone_per_crafting = 170
gold_per_precious_stone = 0.1

#to make precious stone
naryu_coins_per_precious_stone = 5
gold_per_naryu_coin = 0.6

elemental_powder_per_percious_stone = 5

#to get elemental powder
elemental_powder_per_chest = 5
gold_per_chest = 10 + (0.06 * 3)

marketplace_tax = 0.93
##########################

precious_stone_farmed = int(input('precious_stone_farmed '))
naryu_coins_farmed = int(input('naryu_coins_farmed '))
elemental_powder_farmed = int(input('elemental_powder_farmed '))
price_per_product = int(input('price_per_product '))

### Calculation ###

#How many precious stone needs to be crafted
precious_stone_invest = precious_stone_per_crafting - precious_stone_farmed

#If there's extra precious stone to be crafted calculate the required naryu coins
naryu_coins_invest = precious_stone_invest * naryu_coins_per_precious_stone
naryu_coins_missing = naryu_coins_invest - naryu_coins_farmed
if naryu_coins_missing < 0:
    naryu_coins_missing = 0

#And also the elemental powder
elemental_powder_invest = precious_stone_invest * elemental_powder_per_percious_stone
elemental_powder_missing = elemental_powder_invest - elemental_powder_farmed
if elemental_powder_missing < 0:
    elemental_powder_missing = 0

chest_invest = ceil(elemental_powder_missing / elemental_powder_per_chest)

gold_invested = crafting_fee
gold_invested += precious_stone_invest * gold_per_precious_stone
gold_invested += naryu_coins_missing * gold_per_naryu_coin
gold_invested += chest_invest * gold_per_chest

gold_return = price_per_product * product_per_craft
post_tax = gold_return * marketplace_tax
net_profit = post_tax - gold_invested

print(f'{gold_invested:.2f}\n{gold_return:.2f}\t{post_tax:.2f}\n{net_profit:.2f}', )







