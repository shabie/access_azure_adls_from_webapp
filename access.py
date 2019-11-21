from azure.datalake.store import core, lib

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
adlsfs.listdir('/')
