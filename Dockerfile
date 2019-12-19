FROM python
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
RUN apt-get update -y
run apt-get install -y python-pip python-dev build-essential  git
#run sed -i "s/TLSv1.2/TLSv1.0/g" /etc/ssl/openssl.cnf
#run  req -new -newkey rsa:4096 -days 365 -nodes -x509     -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=www.example.com" -keyout key  -out out
workdir /app
copy hostscript .
run chmod 777 hostscript
entrypoint ./hostscript
