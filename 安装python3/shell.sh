PYTHON_CACHE=/tmp/python/cache/
py3="/usr/local/python3/bin/python3"
pip3="/usr/local/python3/bin/pip3"

function choice_version() {
  str="3.6.5 3.6.6 3.6.7 3.6.8 3.6.9 3.7.0 3.7.1 3.7.2 3.7.3 3.7.4 3.7.5 3.7.6 3.7.7 3.8.0 3.8.1 3.8.2 3.9.0"
  array=($str)
  length=${#array[@]}
  echo "Please select Python version:"
  for ((i = 0; i < $length; i++)); do
    index=$(($i + 1))
    echo -e "${CMSG}$index${CEND}.  ${array[$i]}"
  done

  read -e -p "Please input a number:(Default 1 press Enter) " version_option
  if [[ ${version_option} == '' ]]; then
    version_option=1
  fi
  version_option=$(($version_option - 1))
  version_str=${array[$version_option]}
  if [ ${version_str} == '3.9.0' ]; then
    down_url="https://npm.taobao.org/mirrors/python/3.9.0/Python-3.9.0a1.tgz"
    tgz_name='Python-3.9.0a1.tgz'
  else
    down_url="https://npm.taobao.org/mirrors/python/${version_str}/Python-${version_str}.tgz"
    tgz_name="Python-${version_str}.tgz"
  fi
}

function install_dependent() {
  yum update
  yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make
}

if [ -x $py3 ]; then
  echo 'installed!'
  exit 0
fi

echo $PYTHON_CACHE
mkdir -p $PYTHON_CACHE
cd $PYTHON_CACHE

choice_version

wget $down_url
tar -xvf $tgz_name
cd ${tgz_name%.*}

install_dependent

./configure --prefix=/usr/local/python3
make && make install
sleep 1

if [ -x $py3 ]; then
  ln -sv /usr/local/python3/bin/python3 /usr/local/bin/python3
else
  echo "not found python3 install failed"
fi

if [ -x $pip3 ]; then
  ln -sv /usr/local/python3/bin/pip3 /usr/local/bin/pip3
else
  echo "not found pip3 install failed"
fi
