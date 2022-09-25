from planhat.client import Planhat
import settings
import pprint

from planhat import API_URL, API_URL_EU, API_URL_US2

# https://app.planhat.com/developer
planhat_client = Planhat(
    API_URL, settings.SECRETS.tenant_id, settings.SECRETS.api_token
)

companies_data = planhat_client.get_companies()
licenses_data = planhat_client.get_licenses()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(companies_data)
