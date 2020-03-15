# -*- coding: utf-8 -*-

import os
import sys
import time
import Info
import json

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402


def print_order_book(bids_or_asks, bid):
    # order_type can look something like this: "[[205.13, 10.0], [205.12, 34.599], ...]" and it is a list with items
    number_of_bids_or_asks = len(bids_or_asks)
    volume = 0.0
    price = 0.0

    # bid can be something like "[205.26, 34.58]", where "205.26" is the price and "34.58" is the amount
    for bid_or_ask in range(number_of_bids_or_asks):
        price += bids_or_asks[bid_or_ask][0]
        volume += bids_or_asks[bid_or_ask][1]

    if bid:
        print ("Average bid price: %3.3f" % (price / number_of_bids_or_asks))
        print ("Average bid order size: %3.3f" % (volume / number_of_bids_or_asks))
    else:
        print ("Average ask price: %3.3f" % (price / number_of_bids_or_asks))
        print ("Average ask order size: %3.3f" % (volume / number_of_bids_or_asks))


def fetch_order_book(exchange_symbol):
    order_book = kraken.fetch_order_book(exchange_symbol)
    # Taken from https://github.com/ccxt/ccxt/wiki/Manual
    # The structure of a returned order book is as follows:
    # {
    #     'bids': [
    #         [ price, amount ], // [ float, float ]
    #         [ price, amount ],
    #         ...
    #     ],
    #     'asks': [
    #         [ price, amount ],
    #         [ price, amount ],
    #         ...
    #     ],
    #     'timestamp': 1499280391811, // Unix Timestamp in milliseconds (seconds * 1000)
    #     'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
    #     'nonce': 1499280391811, // an increasing unique identifier of the orderbook snapshot
    # }

    for key, order_type in order_book.iteritems():
        if key == 'bids':
            print_order_book(order_type, True)
        elif key == 'asks':
            print_order_book(order_type, False)
        else:
            i = 0
            # print ("Key not handled")


kraken = ccxt.kraken({
    'apiKey': Info.API_KEY,
    'secret': Info.API_SECRET,
    'verbose': True,  # switch it to False if you don't want the HTTP log
})

# Test #1: fetch and display the order book
symbol = 'ETH/EUR'
print("Test 1: Fetch and print the order book")
print("->")
fetch_order_book(symbol)
print("<-")

print(kraken.fetch_balance())

result = ""
maker = 0.0
taker = 0.0

# kraken.fetch_trading_fees(params={info, maker, taker})
# result = kraken.fetch_trading_fees()
# print("maker: " + kraken.maker + '\n' + "taker: " + kraken.taker)
# print("test")
# print(result.items())
# for key, value in result.iteritems() :
#        print( key, value)

# markets = kraken.load_markets()
# print(kraken.id, markets)
# ethereum_ticker = kraken.fetch_ticker('ETH/EUR')
# print(ethereum_ticker)
# for key, value in ethereum_ticker.iteritems() :
#         print( key, value)
#         if key == 'last' :
#             print(value)
# myTrades = kraken.fetch_my_trades('ETH/EUR')
# print(myTrades)

since = kraken.milliseconds() - 86400000  # -1 day from now
# alternatively, fetch from a certain starting datetime
# since = exchange.parse8601('2018-01-01T00:00:00Z')
# all_orders = []
# while since < kraken.milliseconds():
#     symbol = 'ETH/EUR'  # change for your symbol
#     limit = 20  # change for your limit
#     orders = kraken.fetch_orders(symbol, since, limit)
#     if len(orders):
#         since = orders[len(orders) - 1]['timestamp']
#         all_orders += orders
#     else:
#         break

delay = 2  # seconds


# my_trades = kraken.fetch_my_trades(symbol)
# for key, order_list in my_trades.iteritems() :
#     if key == 'bids':
#         print( key, order_list)
#
#         for order in order_list:
#             print (order)
#
#     elif key == 'asks' :
#         print(key, order_list)
#     else:
#         print ("Unknown key")



        # for price, amount in value.iteritems() :
        #     print (price, amount)
# print (order_book)
# time.sleep (delay) # rate limit

# print("" + result)


print("end")
