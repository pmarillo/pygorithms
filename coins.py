#!/bin/python3

import sys
from numpy import cross

def print_change(coins, n):
    make_change(coins, n, n)


def make_change(coins, n):
    quantities = [0 for _ in coins]
    if n == 0: return quantities

    for coin in coins:
        if coin <= n:
            quantities[coins.index(coin)] += 1
            subquantities = make_changes(coins, n - coin)
            if not subquantities:
                continue
            for i in range(len(quantities)):
                quantities[i] += subquantities[i]
            if n == ntot and sum(cross(quantities,coins)) == ntot:
                res_list.append(quantities)
            return quantities
    
res_list = []
n,m = input().strip().split(' ')
ntot,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
make_change(coins, n)

