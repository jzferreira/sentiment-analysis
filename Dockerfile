FROM ubuntu:latest

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && apt-get -y install sudo vim curl wget

RUN pip3 install nltk

ENV CORPORA punkt averaged_perceptron_tagger stopwords wordnet sentiwordnet
RUN python -m nltk.downloader $CORPORA;

WORKDIR /home/sentiment
COPY . /home/sentiment

#ENTRYPOINT ["python", "sentiment.py"]
