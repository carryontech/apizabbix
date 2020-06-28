from pyzabbix import ZabbixAPI
api = ZabbixAPI ("http://127.0.0.1")
api.login("Admin", "zabbix")
host = api.host.create (
{
        "host": "servidor web",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.0.1",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "15"
            }]
}
)
print (host)