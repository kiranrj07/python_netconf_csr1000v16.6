from ncclient import manager

m = manager.connect(host='10.1.1.44', port='830', username='admin',
                    password='root@123', device_params={'name':'csr'}, hostkey_verify=False)

for capability in m.server_capabilities:
  # print('*'* 50)
   print(capability)

m.close_session()
