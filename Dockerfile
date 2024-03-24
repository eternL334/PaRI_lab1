FROM python:3.11-slim

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

COPY src/ /root/src/
RUN chown -R root:root /root/src

WORKDIR /root

CMD ["python3", "src/server.py"]