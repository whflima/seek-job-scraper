# Dockerfile
FROM public.ecr.aws/lambda/python:3.11

# Set the working directory
WORKDIR /var/task

# Install FastAPI, Mangum and other dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the FastAPI app to the container
COPY app app/

# Set the FastAPI app as the Lambda handler using Mangum
CMD ["app.main.handler"]