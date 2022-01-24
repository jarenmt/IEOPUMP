# !/usr/bin/env python
# coding: utf-8
from __future__ import print_function
import logging
from decimal import Decimal as D

from gate_api import ApiClient, Configuration, Order, SpotApi

import time

from config import RunConfig

logger = logging.getLogger(__name__)

def logCurrentTime(logStr):
    timeF = time.time() # Returns unix time in seconds as a float
    timeInt = int(timeF) # Cast to int (remove everything after decimal place)
    timeMs = timeF - timeInt # Get just the ms from the current time
    logger.info(logStr + str(time.strftime("%I:%M:%S.", time.localtime(timeF))) + str(timeMs)[2:])

def logOrderCreateTime(trade):
    orderCreateTime = int(trade.create_time) # Returns unix time that the order was created as an int in seconds
    orderCreateTimeMs = float(trade.create_time_ms) # Returns unix time that the order was created as a float in ms
    print("Order create time: " + time.strftime("%I:%M:%S.", time.localtime(int(orderCreateTime)))
        + str((orderCreateTimeMs / 1000) - float(orderCreateTime))[2:])

def spot_demo(run_config):
    logCurrentTime("Starting program at ")

    # type: (RunConfig) -> None
    currency_pair = "ETH_USDT" # Base_Quote
    # For a buy order, you are selling the quote and receiving the base
    # For a sell order, you are selling the base and receiving the quote
    currency = currency_pair.split("_")[1]

    # Initialize API client
    # Setting host is optional. It defaults to https://api.gateio.ws/api/v4
    config = Configuration(key=run_config.api_key, secret=run_config.api_secret, host=run_config.host_used)
    spot_api = SpotApi(ApiClient(config))
    pair = spot_api.get_currency_pair(currency_pair)
    logger.info("testing against currency pair: " + currency_pair)
    min_amount = pair.min_base_amount

    logCurrentTime("Current time: ")
    timeToPlaceOrder = time.time() + 1

    while(time.time() < timeToPlaceOrder):
        fakeVar = 2

    # get last price
    tickers = spot_api.list_tickers(currency_pair=currency_pair)
    assert len(tickers) == 1
    last_price = tickers[0].last

    # make sure balance is enough
    order_amount = D(min_amount)
    accounts = spot_api.list_spot_accounts(currency=currency)
    assert len(accounts) == 1
    available = D(accounts[0].available)
    logger.info("Account available: %s %s", str(available), currency)
    if available < order_amount:
        logger.error("Account balance not enough")
        return

    price = float(last_price)*1.02
    order = Order(amount=str(order_amount), price=price, side='buy', currency_pair=currency_pair)
    logger.info("place a spot %s order in %s with amount %s and price %s", order.side, order.currency_pair,
                order.amount, order.price)
    logCurrentTime("Creating order at ")
    created = spot_api.create_order(order)
    logger.info("order created with id %s, status %s", created.id, created.status)
    if created.status == 'open':
        order_result = spot_api.get_order(created.id, currency_pair)
        logger.info("order %s filled %s, left: %s", order_result.id, order_result.filled_total, order_result.left)
        result = spot_api.cancel_order(order_result.id, currency_pair)
        most_recent_trade = spot_api.list_my_trades(currency_pair)[0]

        logOrderCreateTime(most_recent_trade)

        #Log difference
        timeDifference = float(most_recent_trade.create_time_ms) / 1000 - timeToPlaceOrder
        logger.info("Difference in timeToPlaceOrder to trade creation time: " + str(timeDifference))

        if result.status == 'cancelled':
            logger.info("order %s cancelled", result.id)
    else:
        trades = spot_api.list_my_trades(currency_pair, order_id=created.id)
        most_recent_trade = spot_api.list_my_trades(currency_pair)[0]

        logOrderCreateTime(most_recent_trade)

        #Log difference
        timeDifference = float(most_recent_trade.create_time_ms) / 1000 - timeToPlaceOrder
        logger.info("Difference in timeToPlaceOrder to trade creation time: " + str(timeDifference))

        # assert len(trades) > 0
        for t in trades:
            logger.info("order %s filled %s with price %s", t.order_id, t.amount, t.price)

    logCurrentTime("Finished at ")