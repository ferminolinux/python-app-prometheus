FROM docker.io/python:alpine3.17

ENV REQUEST_LATENCY 0 

RUN set -exo pipefail ; \
    
    apk add py3-pip ;  \
    
    mkdir /opt/app/ ; \
    adduser -D jojo ; \
    chown -R jojo:jojo /opt/app ; 
        
COPY --chown=jojo:jojo ./app /opt/app

WORKDIR /opt/app

USER jojo

RUN pip install \
    Flask \
    Flask-Markdown \
    Flask-Exceptions \
    prometheus-client ;

EXPOSE 5000

CMD ["python", "jojoba.py"]
        







