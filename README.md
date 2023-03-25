# ecom_api

Step1: install the latest python3 version <br />
Step2: install the pip <br />
step3: pip install virtualenv
step4: python<version> -m venv <virtual-environment-name> <br />
step5: source <virtual-environment-name>/bin/activate <br /> 
step6: pip install -r requirements.txt <br /> 
step7: access the flask app in localhost:5000 with /serach option as `http://localhost:5000/search?q=iphone` <br /> 
<br />
<br />
This is a lightweight process, to increase capacity we can go for the cloud api endpoint + serverless or cloud api endpoint + EKS or AKS or GKE or Cloud api endpoint with baremetal (with HA) <br />

Your implementation should make the process of adding new websites easy without degrading the API performance. The assignment will be evaluated for both desired functionality and maintainability: For this we can go with Cloud api endpoint like api-gateway (AWS) and in background we can add microservices (for each websites) or a serverless lambda jobs this will make the api endpoint is Highly available (Just to make each call as a seperate process ) To make the different website output to combine we can have Fronent layer with amazon and flipkart as module and when we click it and it will do the o/p with respect to its isolated services)

This can be done via single long code aswell,But just considering the performance aspects i believe this architecture will be well suited (even in baremetal with containerization concepts) 
