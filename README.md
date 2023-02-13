# Stake
A simple module for automating Stake, this module avoids detection.

## Overview
This is an informal module using the official API that allows you to transfer, withdraw, and get balance tips on Stake.
By using this module, you can perform various operations in conjunction with Discord Bots, etc.

In the future, there will be methods to play original games such as Dice.

## Features
- You can:
    * Check your own KYC status.
    * Send tip to designated users.
    * Check your balance.
    * Check the information registered in your account.
    * View a list of sessions and delete them.
    * See the list of API keys that have been issued.
    * Withdraw your tip to the address.
    * Get crypto currency and real money rates.

## Install
`pip install -U stake`

## Usage
```python
from stake import Stake

stake = Stake('Your API Key.')

response = stake.user_balances()
for currency in response['data']['user']['balances']:
    print(f"{currency['available']['amount']} {currency['available']['currency'].upper()}")
```

## Legal
This is not official on Twitter. Use at your own risk.
