#!/bin/bash
NSQ_URL="https://0302b-1257892566.cos.ap-guangzhou.myqcloud.com/nsq-1.2.0.linux-amd64.go1.12.9.tar.gz"
IP_ADDR="$(curl ip.sb -s)"
function install_supervisor() {
  yum install -y supervisor
  systemctl enable supervisord.service
  systemctl start supervisord.service
  cat <<EOF >/etc/supervisord.d/web.ini
[inet_http_server]
port=0.0.0.0:5000
EOF
  supervisorctl reload
}

function install_nsq() {
  wget ${NSQ_URL}
  tar zxvf nsq-1.2.0.linux-amd64.go1.12.9.tar.gz
  cd nsq-1.2.0.linux-amd64.go1.12.9/bin/ || exit

}
function nohup_start_nsq() {
  nohup ./nsqlookupd >/dev/null 2>&1 &
  nohup ./nsqd --lookupd-tcp-address=0.0.0.0:4160 --broadcast-address="${IP_ADDR}" >/dev/null 2>&1 &
  nohup ./nsqadmin --lookupd-http-address=0.0.0.0:4161 >/dev/null 2>&1 &
}
function supervisor_start_nsq() {
  cat <<EOF >/etc/supervisord.d/nsqlookupd.ini
[program:nsqlookupd]
command=$(pwd)/nsq-1.2.0.linux-amd64.go1.12.9/bin/nsqlookupd >/dev/null 2>&1 &  ; 程序启动命令
autostart=true       ; 在supervisord启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数，默认是3
user=root          ; 用哪个用户启动进程，默认是root
priority=10         ; 进程启动优先级，默认999，值小的优先启动
redirect_stderr=true ; 把stderr重定向到stdout，默认false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小，默认50MB
stdout_logfile_backups = 20   ; stdout 日志文件备份数，默认是10
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/opt/apache-tomcat-8.0.35/logs/catalina.out
stopasgroup=false     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
killasgroup=false     ;默认为false，向进程组发送kill信号，包括子进程
EOF
  cat <<EOF >/etc/supervisord.d/nsqd.ini
[program:nsqd]
command=$(pwd)/nsq-1.2.0.linux-amd64.go1.12.9/bin/nsqd --lookupd-tcp-address=0.0.0.0:4160 --broadcast-address=${IP_ADDR} >/dev/null 2>&1 &  ; 程序启动命令
autostart=true       ; 在supervisord启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数，默认是3
user=root          ; 用哪个用户启动进程，默认是root
priority=11         ; 进程启动优先级，默认999，值小的优先启动
redirect_stderr=true ; 把stderr重定向到stdout，默认false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小，默认50MB
stdout_logfile_backups = 20   ; stdout 日志文件备份数，默认是10
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/opt/apache-tomcat-8.0.35/logs/catalina.out
stopasgroup=false     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
killasgroup=false     ;默认为false，向进程组发送kill信号，包括子进程
EOF
  cat <<EOF >/etc/supervisord.d/nsqadmin.ini
[program:nsqadmin]
command=$(pwd)/nsq-1.2.0.linux-amd64.go1.12.9/bin/nsqadmin --lookupd-http-address=0.0.0.0:4161 >/dev/null 2>&1 & ; 程序启动命令
autostart=true       ; 在supervisord启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数，默认是3
user=root          ; 用哪个用户启动进程，默认是root
priority=12         ; 进程启动优先级，默认999，值小的优先启动
redirect_stderr=true ; 把stderr重定向到stdout，默认false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小，默认50MB
stdout_logfile_backups = 20   ; stdout 日志文件备份数，默认是10
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/opt/apache-tomcat-8.0.35/logs/catalina.out
stopasgroup=false     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
killasgroup=false     ;默认为false，向进程组发送kill信号，包括子进程
EOF
  supervisorctl reload
}
function test_nsq() {
  echo "wait test nsq ......"
  sleep 3
  postdata=$1
  result=$(curl -d "${postdata}" "http://0.0.0.0:4151/pub?topic=test" -s)
  echo "result=${result}"

}
read -e -r -p "is use the supervisor start nsq?(yes || no):" result
if [ "${result}" == "yes" ]; then
  install_supervisor
  install_nsq
  #  supervisor_start_nsq
  #  test_nsq "fuck you"
  exit
elif [ "${result}" == "no" ]; then
  install_nsq
  nohup_start_nsq
  test_nsq "fuck you"
  exit
else
  echo "${result} not in <yes || no>"
  echo "install is fail!"
  exit
fi
