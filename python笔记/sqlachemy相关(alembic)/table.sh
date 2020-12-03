#!/bin/bash
if [ $# != 1 ]; then
  echo '请输入 表名 文件名'
  exit
fi
flask-sqlacodegen sqlite:///testdb --tables ${1} --outfile "${1}.py"