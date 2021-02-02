FROM python:3
RUN apt-get install -y python
COPY . /src/
CMD ["python", "/src/basic.py"]
