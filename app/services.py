import requests
from django.conf import settings

def qbo_api_call(access_token, realm_id):
    """[summary]
    
    """
    
    if settings.ENVIRONMENT == 'production':
        base_url = settings.QBO_BASE_PROD
    else:
        base_url =  settings.QBO_BASE_SANDBOX

    route = '/v3/company/{0}/companyinfo/{0}'.format(realm_id)
    auth_header = 'Bearer {0}'.format(access_token)
    headers = {
        'Authorization': auth_header, 
        'Accept': 'application/json'
    }
    return requests.get('{0}{1}'.format(base_url, route), headers=headers)


def _qbo_get(access_token, realm_id, route):
    if settings.ENVIRONMENT == 'production':
        base_url = settings.QBO_BASE_PROD
    else:
        base_url = settings.QBO_BASE_SANDBOX

    headers = {
        'Authorization': 'Bearer {0}'.format(access_token),
        'Accept': 'application/json'
    }
    return requests.get('{0}{1}'.format(base_url, route), headers=headers)


def qbo_chart_of_accounts(access_token, realm_id):
    route = '/v3/company/{0}/query?query=SELECT * FROM Account'.format(realm_id)
    return _qbo_get(access_token, realm_id, route)


def qbo_journal_entries(access_token, realm_id):
    route = '/v3/company/{0}/query?query=SELECT * FROM JournalEntry'.format(realm_id)
    return _qbo_get(access_token, realm_id, route)


def qbo_profit_and_loss(access_token, realm_id):
    route = '/v3/company/{0}/reports/ProfitAndLoss?minorversion=69'.format(realm_id)
    return _qbo_get(access_token, realm_id, route)
    