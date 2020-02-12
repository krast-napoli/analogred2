FROM python:3
WORKDIR /usr/src/analogred2
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "./analogred2.py"]