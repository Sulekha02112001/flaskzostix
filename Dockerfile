FROM python:alpine3.7
COPY httpApp/* /app/
WORKDIR /app
RUN pip3 install -r requirement.txt
EXPOSE 8000
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]