import xml.etree.ElementTree as ET



#By FILE
# tree = ET.parse('running.xml')
# root = tree.getroot()

#By String
#root = ET.fromstring(country_data_as_string)



# import xml.etree.ElementTree as ET
# tree = ET.parse('running.xml')
# root = tree.getroot()
# print(root[0][3][0].tag)


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

print("I am printing complete xml here: ",c)

root = ET.fromstring(str(c))
n=int(input("Enter interface number: "))
n=n-1
int_number = list(root)[0][0][0][n][0].text
int_ip = list(root)[0][0][0][n][1][0][0][0].text

print("GigabitEthernet" +int_number+ "IP Address:  "+int_ip)

#c.close_session()