#https://do-hansung.tistory.com/48 을 참조

FROM python:3.7

WORKDIR /app

COPY . /app

RUN python -m pip install git+https://github.com/leehosu01/BibleLM.git@lite
RUN git clone https://github.com/leehosu01/BibleLM.git /opt/app
RUN pip install requests flask

# 5000포트를 외부로 노출함
EXPOSE 5000

#ENV NAME World

CMD ["python", "app.py"]
