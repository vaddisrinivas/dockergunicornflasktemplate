FROM python
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
RUN apt-get update -y
run apt-get install -y python-pip python-dev build-essential  git
workdir /app
copy hostscript .
run chmod 777 hostscript
entrypoint ./hostscript
