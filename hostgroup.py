from pyzabbix import ZabbixAPI

api = ZabbixAPI ("http://127.0.0.1")
api.login("Admin", "zabbix")

hostgroup = api.hostgroup.create(
{"name": "CarryOn Tech 2"}

)

print (hostgroup)