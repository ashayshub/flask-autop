FROM python:3.6.3-jessie
RUN apt-get update && \
     apt-get install git python3-pip -y
RUN git clone https://github.com/ashayshub/flask-autop.git /app
#COPY ./ /app
WORKDIR /app
RUN pip3 install -r requirements.txt

ENV FLASK_APP autop.app
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]
