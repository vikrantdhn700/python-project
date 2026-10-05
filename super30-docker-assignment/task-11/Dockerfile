FROM python:3.11-slim
WORKDIR /app            # sets working directory inside image
COPY requirements.txt ./ # copies files from build context
RUN pip install -r requirements.txt # runs command at build time to install deps
COPY . /app             # copy app files into container
EXPOSE 8000             # documents container listens on this port (informational)
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"] # default runtime command