from ncclient import manager

m = manager.connect(host='10.1.1.44', port='830', username='admin',
                    password='root@123', device_params={'name':'csr'}, hostkey_verify=False)


SCHEMA = m.get_schema('Cisco-IOS-XE-features')
print(SCHEMA)

m.close_session()