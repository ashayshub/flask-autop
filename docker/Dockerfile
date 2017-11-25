FROM python:3.6.3-alpine3.6
RUN apk update
RUN apk add git
RUN git clone https://github.com/ashayshub/flask-autop.git /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP autop.app
RUN pwd
ENTRYPOINT ["python3"]
CMD ["/usr/local/bin/flask", "run"]
