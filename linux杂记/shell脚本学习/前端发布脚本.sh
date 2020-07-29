#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

#BIN_FOLDER = $(cd "$(dirname "$0")",pwd) 解析：
#
#1、取当前运行脚本的所在路径：　$0
#
#2、取当前脚本所在路径的父目录：　dirname "$0"
#
#3、取返回的父目录的值：　$(dirname "$0")
#
#4、cd到返回的父目录：　cd "$(dirname "$0")"
#
#5、输出地址：　cd "$(dirname "$0")",pwd

#6、取输出的地址，并赋值给BIN_FOLDER：　BIN_FOLDER = $(cd "$(dirname "$0")",pwd)

if [ $# -lt 1 ]; then
  echo "订单前端域 发布脚本"
  echo "Usage: $0 <test|prod>"
  echo ""
  echo " - $0 test        # 发布到测试环境"
  echo " - $0 prod        # 发布到生产环境"
  echo ""
  exit 1
fi

test_path=/www/wwwroot/order-fe.ngchat.cn
prod_path=/www/wwwroot/www.yunorder.xyz
test_path=$prod_path

function publish_to() {

  what_path=$1

  \cp ./dist/* $what_path/dist/ -Rrf
  chown www:www $what_path/dist/* -R
}

cd /www/wwwroot/git/order-fe || exit

git pull

echo "发布到测试环境……"

publish_to $test_path

if [[ "$1" == "prod" ]]; then
  echo "发布到生产环境..."
  publish_to $prod_path
fi

echo "订单前端域 发布完成!"
