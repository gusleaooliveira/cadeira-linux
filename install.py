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

instalar=[
"openssh-server",
"vlan",
"isc-dhcp-server",
"bind9",
"dnsutils",
"isc-dhcp-server",
"apache2",
"php7.3",
"libapache2-mod-php7.3",
"php7.3",
"libapache2-mod-perl2",
"libapache2-mod-python",
"python-mysqldb",
"openssl",
"mariadb-server",
"php-pear",
"php7.3-mysql",
"unzip",
"php-imagick php-phpseclib php-php-gettext php7.3-common php7.3-mysql php7.3-gd php7.3-imap php7.3-json php7.3-json",
"php7.3-curl php7.3-zip php7.3-xml php7.3-mbstring php7.3-bz2 php7.3-intl php7.3-gmp",
"postgresql postgresql-contrib",
"phppgadmin",
"acl attr autoconf bind9utils bison build-essential debhelperdnsutils docbook-xml docbook-xsl flex gdb libjansson-dev",
"krb5-user libacl1-dev libaio-devlibarchive-dev libattr1-dev libblkid-dev libbsd-dev libcap-dev libcups2-dev",
"libgnutls28-devlibgpgme-dev libjson-perl libldap2-dev libncurses5-dev libpam0g-dev libparse-yapp-perllibpopt-dev",
"libreadline-dev nettle-dev perl perl-modules-5.28 pkg-config python-all-devpython-crypto python-dbg python-dev",
"python-dnspython python3-dnspython python-gpgpython3-gpg python-markdown python3-markdown python3-dev xsltproc",
"zlib1g-devliblmdb-dev lmdb-utils libdbus-1-dev python3-iso8601 python3-cryptography python3-pyasn1",
"krb5-user krb5-config winbind samba samba-common smbclientcifs-utils libpam-krb5 libpam-winbind libnss-winbind ntp",
"squid"
]

comandos=[
"apt install"
"wget https://files.phpmydamin.net/phpMyAdmin/4.9.0.1/phpMyAdmin-4.9.0.1-all-languages.zip"
]

mensagens=[
"Instalar item:",
"Baixar arquivo:"
]

for item in instalar:
    executar(mensagens[0], comandos[0]+" "+item)

executar(mensagens[1], comandos[1])
