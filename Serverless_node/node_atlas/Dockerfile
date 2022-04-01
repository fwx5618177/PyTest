FROM public.ecr.aws/lambda/nodejs:12

ADD ./server_node/app.js   ./

EXPOSE 9000

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.handler" ]
