FROM public.ecr.aws/lambda/python:3.11

# Copy everything to /var/task (Lambda's working dir)
COPY app/ /var/task/app/
COPY requirements.txt .

# Install dependencies into /var/task
RUN pip install -r requirements.txt --target /var/task

# Set the Lambda entrypoint to your FastAPI Mangum handler
CMD ["app.main.handler"]