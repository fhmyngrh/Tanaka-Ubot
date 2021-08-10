# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Lah U cp Atur atur
# Tanaka-Ubot
#
RUN git clone -b Tanaka-Ubot https://github.com/fhmyngrh/Tanaka-Ubot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/fhmyngrh/Tanaka-Ubot/Tanaka-Ubot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
