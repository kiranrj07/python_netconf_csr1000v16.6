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
<native xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-native'>
<ip>
<route> 
    <ip-route-interface-forwarding-list>
        <prefix>10.10.0.0</prefix>
        <mask>255.255.255.0</mask>
        <fwd-list>
            <fwd>192.168.0.1</fwd>
        </fwd-list>
    </ip-route-interface-forwarding-list>
</route>
</ip>
</native>
</config>
"""

data= m.edit_config(CONFIGURATION, target = 'running')
print(data)
m.close_session()