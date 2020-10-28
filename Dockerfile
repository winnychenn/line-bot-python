FROM python
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
COPY . /
RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]

