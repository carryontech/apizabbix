# API Zabbix

A API do Zabbix permite criar e modificar a configuração do Zabbix e fornece acesso a dados históricos. É amplamente utilizada para: Criar novos aplicativos para trabalhar com o Zabbix;
Integrar o Zabbix com software de terceiros; Automatizar tarefas de rotina. 

A API do Zabbix é uma API baseada na Web e é enviada como parte do front-end da Web. Ela usa o protocolo JSON-RPC 2.0. A estrutura da API consiste em vários métodos que são nominalmente agrupados em APIs separadas. 

Cada um dos métodos executa uma tarefa específica. Por exemplo, o host.create é usado para criar novos hosts. 

A maioria dos APIs contém pelo menos quatro métodos: GET, CRETAT, UPDATE e DELETE para a recuperação, criando, atualização e  exclusão de dados respectivamente, mas algumas das APIs podem fornecer um conjunto totalmente diferente dos métodos. 

Fonte: zabbix.com


Para consunmir a API é necessario ter o python instalado e ajusta o ip do seu sevidor Zabbix dentro dos arquivos
Executar os seguintes comandos:
python hostgroup.py
python host.py
