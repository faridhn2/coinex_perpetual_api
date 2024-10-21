#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from .request_client_v2 import RequestClientV2
import json

class CoinexPerpetualApi2(object):
    ORDER_DIRECTION_SELL = 1
    ORDER_DIRECTION_BUY = 2

    MARGIN_ADJUST_TYPE_INCRESE = 1
    MARGIN_ADJUST_TYPE_DECREASE = 2

    POSITION_TYPE_ISOLATED = 1
    POSITION_TYPE_CROSS_MARGIN = 2

    def __init__(self, access_id, secret_key, logger=None):
        self.request_client = RequestClientV2(access_id, secret_key)

    # System API
    def ping(self):
        """
        # Request
        GET https://api.coinex.com/v2/ping

        # Response
        {
        "code": 0,
        “data”: "pong",
        "message": "ok"
        }
        """
        path = '/ping'
        return self.request_client.request(
        "GET",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        params={},
        )

    # Market API
    
    def get_market_state(self, market):
        """
        # Request
        GET https://api.coinex.com/v2/futures/market
        # Response
        {
            "message": "OK",
            "code": 0,
            "data": {
                "date": 1568097425927,
                "ticker": {
                    "vol": "260102",
                    "low": "6000.0000",
                    "open": "10000.0000",
                    "high": "14999.99999999999999992500",
                    "buy": "6000.0000",
                    "buy_amount": "9998",
                    "sell_amount": "0",
                    "last": "6000.0000",
                    "period": 86400,
                    "position_amount": "10000.0000",
                    "funding_time": 9,
                    "funding_rate_last": "-0.00144",
                    "sell_total": "1321512",
                    "sign_price": "6000",
                    "funding_rate_next": "-0.00375",
                    "insurance": "2.43679741441092111045",
                    "buy_total": "498108",
                    "sell": "0"
                }
            }
        }
        """
        path = '/futures/market'
        params = {
            'market': market
        }
        return self.request_client.request(
        "GET",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        params=params,
        )

    
    # Account API
    def query_account(self):
        """
        # params:
            available	String	账户可用余额
            balance_all	String	账号资产 = available+ frozen + margin_all
            margin_all	String	保证金余额
            margin_position	String	仓位保证金
            frozen	String	冻结额度
            profit_unreal	String	未实现盈亏
            profit_real	String	已实现盈亏

        # Request
        GET https://api.coinex.com/v2/assets/futures/balance
        # Response
        {
            "code": 0,
            "message": "ok",
            "data":
            {
                "BTC": {
                    "balance_total": "1000.00000000000000000000",
                    "transfer": "1000.00000000000000000000",
                    "available": "1000.00000000000000000000",
                    "margin": "0",
                    "frozen": "0"
                },
                "ETH": {
                    "balance_total": "500.00000000000000000000",
                    "transfer": "500.00000000000000000000",
                    "available": "500.00000000000000000000",
                    "margin": "0",
                    "frozen": "0"
                },
            },
            "message": "ok"
        }
        """
        path = '/assets/futures/balance'
        return self.request_client.request(
        "GET",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        params={},
        )

    # Trading API
    def put_limit_order(self, market, side, amount, price):
        """
        # params:
            market	String	Yes	合约市场
            side	String	Yes	委托类型 1表示卖空，2表示买多
            amount	String	Yes	委托数量
            price	String	Yes	委托价格
            
        # Request
        POST https://api.coinex.com/v2/futures/order
        {
            "market": "CETUSDT",
            "market_type": "FUTURES",
            "side": "buy",
            "type": "limit",
            "amount": "10000",
            "price": "1",
            "client_id": "user1",
            "is_hide": true
        }

        # Response
        {
          "code": 0,
          "data": {
              "order_id": "13400",
              "market": " CETUSDT",
              "market_type": "FUTURES",
              "side": "buy",
              "type": "limit",
              "amount": "10000",
              "price": "1",
              "unfilled_amount": "50241.7185224371",
              "filled_amount": "27564.87468358",
              "filled_value": "27564.87468358",
              "client_id": "client_id_1",
              "fee": "11.6582326221",
              "fee_ccy": "USDT",
              "maker_fee_rate": "0",
              "taker_fee_rate": "0.0003",
              "last_filled_amount": "27564.87468358",
              "last_filled_price": "1",
              "realized_pnl": "-22.142539215",
              "created_at": 1691482451000,
              "updated_at": 1691482451000
          },
          "message": "OK"
      }
        """
        path = '/futures/order'
        data = {
            'market': market,
            "market_type": "FUTURES",
            "side": str(side),
            "type": "limit",
            "amount": str(amount),
            "price": str(price),
        }
        data = json.dumps(data)
        return self.request_client.request(
        "POST",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        data=data,
        )

    def put_market_order(self, market, side, amount):
        """
        # params:
            market	String	Yes	合约市场
            side	String	Yes	委托类型 1表示卖空，2表示买多
            amount	String	Yes	委托数量

        # Request
        POST https://api.coinex.com/v2/futures/order
        {
            "market": "CETUSDT",
            "market_type": "FUTURES",
            "side": "buy",
            "type": "market",
            "amount": "10000",
            "client_id": "user1",
            "is_hide": true
        }

        # Response
        {
        "code": 0,
        "data": {
            "order_id": "13400",
            "market": " CETUSDT",
            "market_type": "FUTURES",
            "side": "buy",
            "type": "limit",
            "amount": "10000",
            "price": "1",
            "unfilled_amount": "50241.7185224371",
            "filled_amount": "27564.87468358",
            "filled_value": "27564.87468358",
            "client_id": "client_id_1",
            "fee": "11.6582326221",
            "fee_ccy": "USDT",
            "maker_fee_rate": "0",
            "taker_fee_rate": "0.0003",
            "last_filled_amount": "27564.87468358",
            "last_filled_price": "1",
            "realized_pnl": "-22.142539215",
            "created_at": 1691482451000,
            "updated_at": 1691482451000
        },
        "message": "OK"
    }
        """
        path = '/futures/order'
        data = {
            'market': market,
            "market_type": "FUTURES",
            "side": str(side),
            "type": "market",
            "amount": str(amount),
        }
        data = json.dumps(data)
        return self.request_client.request(
        "POST",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        data=data,
        )

    
    
    def cancel_all_order(self, market):
        """
        # Request
        POST https://api.coinex.com/v2/futures/cancel-all-order
        # Request.Body
        {
            "market": "CETUSDT",
            "market_type": "FUTURES",
            "side": "sell"
        }

        # Response
        {
             "code": 0,
            "data": {},
            "message": "OK"
        }
        """
        path = '/futures/cancel-all-order'
        data = {
            'market': market,
            "market_type": "FUTURES",
            
        }
        data = json.dumps(data)
        return self.request_client.request(
        "POST",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        data=data,
        )
    
    def stop_position(self, market):
        """
        # Request
        POST https://api.coinex.com/v2/futures/close-position
        # Request.Body
        {
            "market": "CETUSDT",
            "market_type": "FUTURES",
            "type": "limit",
            "price": "0.056",
            "amount": "10000",
            "client_id": "user1",
            "is_hide": true
        }

        # Response
        {
            "code": 0,
            "data": {
                "order_id": "13400",
                "market": " CETUSDT",
                "market_type": "FUTURES",
                "side": "buy",
                "type": "limit",
                "amount": "10000",
                "price": "1",
                "unfilled_amount": "50241.7185224371",
                "filled_amount": "27564.87468358",
                "filled_value": "27564.87468358",
                "client_id": "client_id_1",
                "fee": "11.6582326221",
                "fee_ccy": "USDT",
                "maker_fee_rate": "0",
                "taker_fee_rate": "0.0003",
                "last_filled_amount": "27564.87468358",
                "last_filled_price": "1",
                "realized_pnl": "-22.142539215",
                "created_at": 1691482451000,
                "updated_at": 1691482451000
            },
            "message": "OK"
        }
        """
        path = '/futures/close-position'
        data = {
            'market': market,
            "market_type": "FUTURES",
            "type": "market",
            
        }
        data = json.dumps(data)
        return self.request_client.request(
        "POST",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        data=data,
        )

    def adjust_leverage(self, market,margin_mode,leverage):
        """
        # Request
        POST https://api.coinex.com/v2/futures/adjust-position-leverage
        # Request.Body
        {
            "market": "CETUSDT",
            "market_type": "FUTURES",
            "margin_mode": "cross",
            "leverage": 10
        }

        # Response
        {
            "code": 0,
            "data": {
                "margin_mode": "cross",
                "leverage": 10
            },
            "message": "OK"
        }
        """
        path = '/futures/adjust-position-leverage'
        data = {
            'market': market,
            "market_type": "FUTURES",
            "margin_mode": margin_mode,
            "leverage": leverage
            
        }
        data = json.dumps(data)
        return self.request_client.request(
        "POST",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        data=data,
        )
    def cancel_order(self, market, order_id):
        """
        # Request
        POST https://api.coinex.com/v2/futures/cancel-order
        # Request.Body
        {
            "market": "CETUSDT",
            "market_type": "FUTURES",
            "order_id": 13400
        }

        # Response
        {
            "code": 0,
            "data": {
                "order_id": 13400,
                "market": " CETUSDT",
                "market_type": "FUTURES",
                "side": "buy",
                "type": "limit",
                "amount": "10000",
                "price": "1",
                "unfilled_amount": "50241.7185224371",
                "filled_amount": "27564.87468358",
                "filled_value": "27564.87468358",
                "client_id": "client_id_1",
                "fee": "11.6582326221",
                "fee_ccy": "USDT",
                "maker_fee_rate": "0",
                "taker_fee_rate": "0.0003",
                "last_filled_amount": "27564.87468358",
                "last_filled_price": "1",
                "realized_pnl": "-22.142539215",
                "created_at": 1691482451000,
                "updated_at": 1691482451000
            },
            "message": "OK"
        }
        """
        path = '/futures/cancel-order'
        data = {
            'market': market,
            "market_type": "FUTURES",
            'order_id': order_id
        }
        data = json.dumps(data)
        return self.request_client.request(
        "POST",
        "{url}{request_path}".format(url=self.request_client.url, request_path=path),
        data=data,
        )

    
if __name__ == "__main__":
    access_id = ''
    secret_key = ''
    api = CoinexPerpetualApi2(access_id, secret_key)
    print(api.ping())
