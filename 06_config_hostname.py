from ncclient import manager

router = {
   'ip': '10.1.1.44',
   'port': '830',
   'username': 'admin',
   'password': 'root@123'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxr'}, hostkey_verify=False)

CONFIGURATION = """
<config>
    <native
        xmlns='http://cisco.com/ns/yang/Cisco-IOS-XE-native'>
        <hostname>config_by_python</hostname>
    </native>
</config> """

data= m.edit_config(CONFIGURATION, target = 'running')
print(data)
m.close_session()