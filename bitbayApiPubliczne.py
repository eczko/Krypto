#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time
from bitbay import get_bitbay_withdrawals

# waluty dostepne na bit bay: pozniez zamienic na zaczyt z api/parsowanie
waluty_bitbay = ['BTC', 'LTC', 'ETH']


# get info from public api



def znajdz_koszt_wycofania(waluta, koszt_wycofania):
    for waluta_koszt in koszt_wycofania:
        if waluta_koszt[0] == waluta:
            return waluta_koszt[1]


def zwroc_koszt_wycofania(waluta, waluta2):
    time.sleep(1)
    koszt_wycofania_bitbay = get_bitbay_withdrawals()
    response = requests.get("https://bitbay.net/API/Public/" + waluta + waluta2 + "/orderbook.json")
    data = response.json()
    # print data
    bids = data['bids']
    bid = []
    for item in bids:
        bid.append(item)
    return ('pierwsza: ', waluta, str(bid[0][0]) + " " + waluta2, str(bid[0][1]) + " volum",
            znajdz_koszt_wycofania(waluta, koszt_wycofania_bitbay) * bid[0][0])


def main():
    # sprawdzenie kosztu wycofrania w zlotowkach
    for waluta in waluty_bitbay:
        print zwroc_koszt_wycofania(waluta, "PLN")


if __name__ == '__main__':
    main()
