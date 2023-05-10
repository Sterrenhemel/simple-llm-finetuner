FROM runpod/pytorch:3.10-2.0.0-117

RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
ENV CLI_ARGS=""
CMD python app.py ${CLI_ARGS}