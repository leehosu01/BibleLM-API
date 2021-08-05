#https://do-hansung.tistory.com/48 을 참조

FROM python:3.7

WORKDIR /app

COPY . /app

RUN python -m pip install git+https://github.com/leehosu01/BibleLM.git@lite

RUN apt-get install git -y

USER root
RUN mkdir /model_file
RUN chmod 777 /model_file
RUN git clone https://github.com/leehosu01/BibleLM.git /model_file
RUN pip install requests flask flask_cors

# 5000포트를 외부로 노출함
EXPOSE 5000

#ENV NAME World

CMD ["python", "app.py"]
