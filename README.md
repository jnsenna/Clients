# Clients
To test:
  Download the file called "access_clients.py".
  
  In the terminal, navigate to the directory containing the folder with "access_clients.py", "requirements.txt", and "Dockerfile".\n
  Create a docker image by running the command <code>docker build Clients</code>.\n
  Before publishing the image, version it by running the command <code>docker tag Clients:latest Clients:0.1</code>.\n
  To create persistent data, run the commands <code>kubectl create -f persistent_volume.yml</code> and <code>kubectl create -f persistent_volume_claim.yml</code>.\n
  To deploy to Kubernetes, run the commands <code>kubectl create -f Clients.deployment.yml</code> and <code>kubectl create -f Clients.service.yml</code>.\n
  To verify that the application is running, run the command <code>kubectl</code>.\n
  </break>
  Tutorials used: 
  https://github.com/nanjekyejoannah/k8s_python_sample_code/tree/master
  https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
