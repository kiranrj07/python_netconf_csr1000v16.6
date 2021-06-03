from ncclient import manager, xml_

router = {
   'ip': '10.1.1.44',
   'port': '830',
   'username': 'admin',
   'password': 'root@123'
}

m = manager.connect(host=router['ip'], port=router['port'], username=router['username'],
                    password=router['password'], device_params={'name':'iosxr'}, hostkey_verify=False)


SAVE = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""

reply=m.dispatch(xml_.to_ele(SAVE))
print(reply)
m.close_session()