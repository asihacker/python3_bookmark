#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"

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
