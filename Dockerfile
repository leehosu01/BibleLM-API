#https://do-hansung.tistory.com/48 을 참조

FROM python:3.7

COPY . /app
WORKDIR /app
USER root


RUN python -m pip install git+https://github.com/leehosu01/BibleLM.git@lite

RUN apt-get install git -y

RUN git clone https://github.com/leehosu01/BibleLM.git
RUN pip install requests flask flask_cors

USER root
RUN chmod 755 /app

# 5000포트를 외부로 노출함
EXPOSE 5000

#ENV NAME World

CMD ["python", "app.py"]
