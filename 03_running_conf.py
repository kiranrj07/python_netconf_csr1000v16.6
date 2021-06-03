from ncclient import manager

router = {
   'ip': '10.1.1.44',
   'port': '830',
   'username': 'admin',
   'password': 'root@123'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'csr'}, hostkey_verify=False)

c = m.get_config(source='running')

print(c)

#############Save config to xml file
save = open('running.xml','w')
save.write(str(c))
save.close()
m.close_session()  