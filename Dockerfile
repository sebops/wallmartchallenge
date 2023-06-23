FROM python:3.12.0b3-alpine3.18
WORKDIR /app
COPY requirements.txt ./
COPY main.py ./
RUN pip install -r requirements.txt
EXPOSE 80
CMD [ "python3" ,"main.py" ]