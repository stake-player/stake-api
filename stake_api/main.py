import requests
from typing import Optional

ENDPOINT = "https://stake.com/_api/graphql"

class Stake:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.headers = {
            'authority': 'stake.com',
            'accept': '*/*',
            'accept-language': 'ja,en-US;q=0.9,en;q=0.8,ja-JP;q=0.7,zh-CN;q=0.6,zh;q=0.5,ru;q=0.4',
            'content-type': 'application/json',
            'origin': 'https://stake.com',
            'referer': 'https://stake.com/',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'x-access-token': access_token,
        }
        self.session = requests.Session()

    def user_balances(self) -> dict:
        json_data = {
            'query': 'query UserBalances {\n  user {\n    id\n    balances {\n      available {\n        amount\n        currency\n        __typename\n      }\n      vault {\n        amount\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            'operationName': 'UserBalances',
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def currency_conversion_rate(self) -> dict:
        json_data = {
            'query': 'query CurrencyConversionRate {\n  info {\n    currencies {\n      name\n      eur: value(fiatCurrency: eur)\n      jpy: value(fiatCurrency: jpy)\n      usd: value(fiatCurrency: usd)\n      brl: value(fiatCurrency: brl)\n      cad: value(fiatCurrency: cad)\n      cny: value(fiatCurrency: cny)\n      idr: value(fiatCurrency: idr)\n      inr: value(fiatCurrency: inr)\n      krw: value(fiatCurrency: krw)\n      php: value(fiatCurrency: php)\n      rub: value(fiatCurrency: rub)\n      mxn: value(fiatCurrency: mxn)\n      dkk: value(fiatCurrency: dkk)\n    }\n  }\n}\n',
            'variables': {},
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def user_kyc_info(self) -> dict:
        json_data = {
            'query': 'query UserKycInfo {\n  isDiscontinuedBlocked\n  user {\n    id\n    roles {\n      name\n      __typename\n    }\n    kycStatus\n    dob\n    createdAt\n    isKycBasicRequired\n    isKycExtendedRequired\n    isKycFullRequired\n    isKycUltimateRequired\n    hasEmailVerified\n    phoneNumber\n    hasPhoneNumberVerified\n    email\n    registeredWithVpn\n    isBanned\n    isSuspended\n    kycBasic {\n      ...UserKycBasic\n      __typename\n    }\n    kycExtended {\n      ...UserKycExtended\n      __typename\n    }\n    kycFull {\n      ...UserKycFull\n      __typename\n    }\n    kycUltimate {\n      ...UserKycUltimate\n      __typename\n    }\n    veriffStatus\n    jpyAlternateName: cashierAlternateName(currency: jpy) {\n      firstName\n      lastName\n      __typename\n    }\n    nationalId\n    outstandingWagerAmount {\n      currency\n      amount\n      progress\n      __typename\n    }\n    activeRollovers {\n      id\n      active\n      user {\n        id\n        __typename\n      }\n      amount\n      lossAmount\n      createdAt\n      note\n      currency\n      expectedAmount\n      expectedAmountMin\n      progress\n      activeBets {\n        id\n        iid\n        game {\n          id\n          slug\n          name\n          __typename\n        }\n        bet {\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserKycBasic on UserKycBasic {\n  active\n  address\n  birthday\n  city\n  country\n  createdAt\n  firstName\n  id\n  lastName\n  phoneNumber\n  rejectedReason\n  status\n  updatedAt\n  zipCode\n  occupation\n}\n\nfragment UserKycExtended on UserKycExtended {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycFull on UserKycFull {\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n\nfragment UserKycUltimate on UserKycUltimate {\n  id\n  active\n  createdAt\n  id\n  rejectedReason\n  status\n}\n',
            'operationName': 'UserKycInfo',
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def send_tip_meta(self, name: Optional[str] = None) -> dict:
        json_data = {
            'query': 'query SendTipMeta($name: String) {\n  user(name: $name) {\n    id\n    name\n    __typename\n  }\n  self: user {\n    id\n    hasTfaEnabled\n    isTfaSessionValid\n    balances {\n      available {\n        amount\n        currency\n        __typename\n      }\n      vault {\n        amount\n        currency\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            'operationName': 'SendTipMeta',
            'variables': {},
        }
        if name:
            json_data['variables']['name'] = name
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def tip_limit(self, currency: str) -> dict:
        json_data = {
            'query': 'query TipLimit($currency: CurrencyEnum!) {\n  info {\n    currency(currency: $currency) {\n      tipMin {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            'operationName': 'TipLimit',
            'variables': {
                'currency': currency,
            },
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def send_tip(self, user_id: str, amount: float, currency: str, is_public: bool = True, tfa_token: Optional[str] = None) -> dict:
        json_data = {
            'query': 'mutation SendTip($userId: String!, $amount: Float!, $currency: CurrencyEnum!, $isPublic: Boolean, $chatId: String!, $tfaToken: String) {\n  sendTip(\n    userId: $userId\n    amount: $amount\n    currency: $currency\n    isPublic: $isPublic\n    chatId: $chatId\n    tfaToken: $tfaToken\n  ) {\n    id\n    amount\n    currency\n    user {\n      id\n      name\n      __typename\n    }\n    sendBy {\n      id\n      name\n      balances {\n        available {\n          amount\n          currency\n          __typename\n        }\n        vault {\n          amount\n          currency\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
            'operationName': 'SendTip',
            'variables': {
                'userId': user_id,
                'amount': amount,
                'currency': currency,
                'isPublic': is_public,
                'chatId': 'c65b4f32-0001-4e1d-9cd6-e4b3538b43ae'
            }
        }
        if tfa_token:
            json_data['variables']['tfaToken'] = tfa_token
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def user_phone_meta(self) -> dict:
        json_data = {
            'query': 'query UserPhoneMeta {\n  user {\n    ...UserPhoneFragment\n    __typename\n  }\n}\n\nfragment UserPhoneFragment on User {\n  id\n  phoneNumber\n  phoneCountryCode\n  hasPhoneNumberVerified\n}\n',
            'operationName': 'UserPhoneMeta',
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def user_email_meta(self) -> dict:
        json_data = {
            'query': 'query UserEmailMeta {\n  user {\n    ...UserEmailFragment\n  }\n}\n\nfragment UserEmailFragment on User {\n  id\n  email\n  hasEmailVerified\n  hasEmailSubscribed\n}\n',
            'variables': {},
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def session_list(self, offset: int = 0, limit: int = 10, name: Optional[str] = None) -> dict:
        json_data = {
            'query': 'query SessionList($offset: Int = 0, $limit: Int = 10, $name: String) {\n  user(name: $name) {\n    id\n    sessionList(offset: $offset, limit: $limit) {\n      ...UserSession\n    }\n  }\n}\n\nfragment UserSession on UserSession {\n  id\n  sessionName\n  ip\n  country\n  city\n  active\n  updatedAt\n}\n',
            'variables': {
                'offset': 0,
                'limit': 10,
            },
        }
        if name:
            json_data['variables']['name'] = name
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def user_community_preferences(self) -> dict:
        json_data = {
            'query': 'query UserCommunityPreferences {\n  user {\n    id\n    community {\n      preferences {\n        rainExclude\n      }\n    }\n  }\n}\n',
            'variables': {},
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def create_withdrawal_meta(self):
        json_data = {
            'query': 'query CreateWithdrawalMeta {\n  user {\n    id\n    hasTfaEnabled\n    balances {\n      ...UserBalanceFragment\n      __typename\n    }\n    __typename\n  }\n  info {\n    currencies {\n      name\n      withdrawalFee {\n        value\n        __typename\n      }\n      withdrawalMin {\n        value\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserBalanceFragment on UserBalance {\n  available {\n    amount\n    currency\n    __typename\n  }\n  vault {\n    amount\n    currency\n    __typename\n  }\n}\n',
            'operationName': 'CreateWithdrawalMeta',
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def create_withdrawal(self, currency: str, address: str, amount: float, chain: Optional[str] = None, email_code: Optional[str] = None, tfa_token: Optional[str] = None, oauth_token: Optional[str] = None) -> dict:
        json_data = {
            'query': 'mutation CreateWithdrawal($chain: CryptoChainEnum, $currency: CryptoCurrencyEnum!, $address: String!, $amount: Float!, $emailCode: String, $tfaToken: String, $oauthToken: String) {\n  createWithdrawal(\n    chain: $chain\n    currency: $currency\n    address: $address\n    amount: $amount\n    emailCode: $emailCode\n    tfaToken: $tfaToken\n    oauthToken: $oauthToken\n  ) {\n    id\n    __typename\n  }\n}\n',
            'operationName': 'CreateWithdrawal',
            'variables': {
                'currency': currency,
                'address': address,
                'amount': amount,
            }
        }
        if chain:
            json_data['variables']['chain'] = chain
        if email_code:
            json_data['variables']['emailCode'] = email_code
        if tfa_token:
            json_data['variables']['tfaToken'] = tfa_token
        if oauth_token:
            json_data['variables']['oauthToken'] = oauth_token
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def get_user_country(self):
        json_data = {
            'query': 'query GetUserCountry {\n  getFeatureFlags {\n    country\n    __typename\n  }\n}\n',
            'operationName': 'GetUserCountry',
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def user_api_keys(self, name: Optional[str] = None):
        json_data = {
            'query': 'query UserApiKeys($name: String) {\n  user(name: $name) {\n    id\n    apiKeys {\n      id\n      ip\n      active\n      sessionName\n      type\n      createdAt\n      updatedAt\n    }\n  }\n}\n',
            'variables': {},
        }
        if name:
            json_data['variables']['name'] = name
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def terminate_session(self, session_id: str):
        json_data = {
            'query': 'mutation TerminateSession($sessionId: String!) {\n  terminateSession(sessionId: $sessionId) {\n    ...UserSession\n    __typename\n  }\n}\n\nfragment UserSession on UserSession {\n  id\n  sessionName\n  ip\n  country\n  city\n  active\n  updatedAt\n}\n',
            'operationName': 'TerminateSession',
            'variables': {
                'sessionId': session_id,
            },
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()
    
    def ignored_user_list(self, offset: int = 0, limit: int = 10) -> dict:
        json_data = {
            'query': 'query IgnoredUserList($offset: Int = 0, $limit: Int = 10) {\n  user {\n    id\n    ignoredUserList(limit: $limit, offset: $offset) {\n      ignoredUser {\n        ...UserTags\n      }\n    }\n  }\n}\n\nfragment UserTags on User {\n  id\n  name\n  isMuted\n  isRainproof\n  isIgnored\n  isHighroller\n  isSportHighroller\n  leaderboardDailyProfitRank\n  leaderboardDailyWageredRank\n  leaderboardWeeklyProfitRank\n  leaderboardWeeklyWageredRank\n  flags {\n    flag\n    rank\n    createdAt\n  }\n  roles {\n    name\n    expireAt\n    message\n  }\n  createdAt\n}\n',
            'variables': {},
        }
        if offset:
            json_data['variables']['offset'] = offset
        if limit:
            json_data['variables']['limit'] = limit
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def update_user_password_meta(self):
        json_data = {
            'query': 'query UpdateUserPasswordMeta {\n  user {\n    id\n    hasPassword\n  }\n}\n',
            'variables': {},
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def request_uset_tfa(self):
        json_data = {
            'query': 'mutation requestUserTfa {\n  requestUserTfa\n}\n',
            'operationName': 'requestUserTfa',
        }
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()

    def request_enable_user_tfa(self, password: Optional[str] = None, tfa_token: Optional[str] = None, oauth_token: Optional[str] = None):
        json_data = {
            'query': 'mutation RequestEnableUserTfa($password: String, $tfaToken: String!, $oauthToken: String) {\n  requestEnableUserTfa(\n    password: $password\n    tfaToken: $tfaToken\n    oauthToken: $oauthToken\n  ) {\n    id\n    __typename\n  }\n}\n',
            'operationName': 'RequestEnableUserTfa',
            'variables': {},
        }
        if password:
            json_data['variables']['password'] = password
        if tfa_token:
            json_data['variables']['tfaToken'] = tfa_token
        if oauth_token:
            json_data['variables']['oauthToken'] = oauth_token
        response = self.session.post(ENDPOINT, headers=self.headers, json=json_data)
        return response.json()
