
FROM  python:3.8-slim-buster

ENV MODEL_ENGINE "text-davinci-002"


COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP "gpt3_script.py"
ENV FLASK_ENV "development"

CMD ["flask", "run", "--host=127.0.0.1"]