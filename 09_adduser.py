from ncclient import manager

router = {
   'ip': '10.1.1.44',
   'port': '830',
   'username': 'admin',
   'password': 'root@123'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxr'}, hostkey_verify=False)



#config route
CONFIGURATION = """
<config>
<native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
       
        <username>
                <name>netconf</name>
                <privilege>15</privilege>
                <password>
                    <encryption>0</encryption>
                    <password>root@123</password>
                </password>
            </username>
</native>
</config>
"""


data= m.edit_config(CONFIGURATION, target = 'running')
print(data)
m.close_session()