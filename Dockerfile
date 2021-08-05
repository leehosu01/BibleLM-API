#https://do-hansung.tistory.com/48 을 참조

FROM python:3.7

WORKDIR /app

COPY . /app

RUN python -m pip install git+https://github.com/leehosu01/BibleLM.git
RUN pip install requests flask

# 80포트를 외부로 노출함
EXPOSE 5000

#ENV NAME World

CMD ["python", "app.py"]
