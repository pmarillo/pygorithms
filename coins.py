#!/usr/bin/python3

import sys



def make_change(coins, num):
    if num == 0: return [0 for _ in coins]

    for coin in coins:
        if coin <= num:
            quantities = [0 for _ in coins]
            updated_quantities = []
            quantities[coins.index(coin)] += 1
            subquantities = make_change(coins, num - coin)
            if not subquantities:
                continue
            for i in range(len(quantities)):
                updated_quantities.append(quantities[i] + subquantities[i])
            if num == ntot and sum([q*c for q, c in zip(updated_quantities,coins)]) == ntot:
                res_list.append(updated_quantities)
            return updated_quantities # XXX yield?

res_list = []
n,m = input().strip().split(' ')
ntot,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
make_change(coins, ntot)
print(len(res_list))
