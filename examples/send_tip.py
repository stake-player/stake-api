from stake_api import Stake

stake = Stake('API_KEY')
response = stake.send_tip_meta('target_username')
response = stake.send_tip(response['data']['user']['id'], 0.0001, 'ltc')
print(response)
