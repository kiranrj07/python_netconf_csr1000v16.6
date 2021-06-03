from ncclient import manager

router = {
   'ip': '10.1.1.44',
   'port': '830',
   'username': 'admin',
   'password': 'root@123'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxr'}, hostkey_verify=False)

# FILTER = """
# <filter>
# <native
#         xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
#         <interface></interface>
# </native>
# </filter> """



FILTER = """
<filter>
<native
        xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface><GigabitEthernet><name>1</name></GigabitEthernet></interface>
</native>
</filter> """

c = m.get_config('running',FILTER)

print(c)

#c.close_session()