# Access ADLS (Azure Data Lake Store) from Azure WebApps

Code snippet to explain how to access ADLS from Azure Web Apps directly:


```python
# test_conn.py
from azure.datalake.store import core, lib

# pro tip: read them from environment variables
tenant_id = 'YOUR_TENANT_ID'
client_id = 'YOUT_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
resource = 'https://datalake.azure.net/'

adls_creds = lib.auth(tenant_id=tenant_id,
		      client_id=client_id,
		      client_secret=client_secret,
		      resource=resource,
		     )
			  
adlsfs = core.AzureDLFileSystem(adls_creds, 'YOUR_ADLS_NAME')
print(adlsfs.listdir('/')) # sanity check: returns the root folder contents of the ADLS
```

Environment variables in the Web App in Azure can be set using the __Application Settings__. See this link for details: https://docs.microsoft.com/en-us/azure/app-service/configure-common

One way to test if this is working is to execute this script from a VM inside extollo using bash. First install the library using:
```bash
pip install azure-datalake-store
```
and then execute the script:
```bash
python test_conn.py
```
