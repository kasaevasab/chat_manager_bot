FROM python:3

WORKDIR /home/sabina/hse_cs/second_course/python_adv_course/chat_manager_bot

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./main.py"]
