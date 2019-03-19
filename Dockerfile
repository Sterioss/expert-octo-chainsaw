FROM python:latest
WORKDIR /workspace/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT["python"]
CMD["main.py"]