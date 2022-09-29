from planhat.client import Planhat
import settings
import pandas as pd
import pandas_gbq
from google.oauth2.service_account import Credentials

from planhat import API_URL, API_URL_EU, API_URL_US2

# https://app.planhat.com/developer
planhat_client = Planhat(
    API_URL, settings.SECRETS.tenant_id, settings.SECRETS.api_token
)

companies_data = planhat_client.get_companies()
licenses_data = planhat_client.get_licenses()

# df = pd.json_normalize(licenses_data)
df = pd.DataFrame(licenses_data)

credentials = Credentials.from_service_account_file(
    "/Users/viktorgrunwald/Documents/Programming/planhat-python/service_account_bq_licenses.json"
)
target_table = "dbtcourse-356512.planhat_data.test_licenses"
project_id = "dbtcourse-356512"
job_location = "EU"

pandas_gbq.to_gbq(
    df,
    target_table,
    project_id=project_id,
    credentials=credentials,
    if_exists="replace",
)

print(df)