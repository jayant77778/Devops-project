FROM redhat/ubi8

RUN yum install -y python3 && \
    pip3 install flask

COPY app.py /app.py

CMD [ "python3", "/app.py" ]
