FROM public.ecr.aws/lambda/python:3.8

# Copy function code and package.json
ADD app.py   ./

EXPOSE 9000

# Set the CMD to your handler
CMD ["app.handler"]