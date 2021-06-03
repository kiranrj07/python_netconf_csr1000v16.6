from ncclient import manager

router = {
   'ip': '10.1.1.44',
   'port': '830',
   'username': 'admin',
   'password': 'root@123'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'csr'}, hostkey_verify=False)
                    
SCHEMA = m.get_schema('ietf-interfaces')


print(SCHEMA)
m.close_session()
