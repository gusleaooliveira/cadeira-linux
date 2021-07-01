#!/usr/bin/env bash

dialog --infobox "Copiando o arquivo:" 30 50 && sleep 2 && clear
mv interfaces /etc/network/interfaces
dialog --infobox "Reiniciando placas de rede:" 30 50 && sleep 2 && clear
ifdown -a && ifup -a

systemctl restart networking
ping 8.8.8.8
ping www.senacrs.com.br
iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sysctl -p
cat /etc/apt/sources.list
apt update
echo "Acquire"  >> /etc/apt/apt.conf.d/99force-ipv4
