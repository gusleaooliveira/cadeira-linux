import os

def executar(mensagem, comando):
    print(mensagem)
    os.system(comando)
    print("")

def executarMuitos(mensagens, comandos):
    for indice, mensagem in enumerate(mensagens):
        executar(mensagem, comandos[indice])


def verificar(mensagem):
    valor=input(mensagem).lower()[0]
    print(valor)
    print("")
    if valor == 's':
        return valor
    elif valor == 'n':
        return valor
    else:
        return verificar(mensagem)


print("Aula 01:")
mensagens=[
    "Copiando o arquivo pro servidor!",
    "Flush nas interfaces!",
    "Reiniciar as interfaces"
    ]
comandos=[
    'mv /servidor/etc/network/interfaces /etc/network/interfaces',
    'ifdown -a && ifup -a',
    'systemctl restart networking'
    ]
executarMuitos(mensagens, comandos)
execPing=verificar("Deseja executar o ping?")
if execPing == 's':
    mensagens=["Executando Ping:", "Inserindo dns:", "Executando Ping:"]
    comandos=['ping 8.8.8.8', 'echo "nameserver 8.8.8.8" > /etc/resolv.conf', 'ping www.senacrs.com.br']
    executarMuitos(mensagens, comandos)

mensagens=[
    "Executando iptables:",
    "Ip forward:",
    "Listando apt list:",
    "Atualizar apt:",
    "99-force-ipv4",
    "Atualizar apt:",
    ]
comandos=[
    'iptables -t nat -A POSTROUTING –o enp0s3 –j MASQUERADE',
    'echo 1>/proc/sys/net/ipv4/ip_forward',
    'cat /etc/apt/sources.list',
    'apt update',
    'echo "Acquire::ForceIPv4 \"true\";" > /etc/apt/apt.conf.d/99force-ipv4',
    'apt update',

    ]
executarMuitos(mensagens, comandos)
