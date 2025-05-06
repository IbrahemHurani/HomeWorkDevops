From python:3.11
WORKDIR /app
COPY . .
RUN pip install flask
RUN mkdir /logs
VOLUME ["/logs"]
CMD ["python", "app.py"]
