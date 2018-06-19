Exercise 1 Launch POD Without POD Manifest

#Launch a Deployment
kubectl run webpod01 --image=nxgcloud/simpleweb:0.0.1 --port=5000

#Get the list of deployments
kubectl get deployments
kubectl get deployments -o wide

#Get the list of pods
kubectl get pods
kubectl get pods -o wide 

#record pod ip
kubectl get pods -o wide 
kubectl describe pod webpod01-67b47f896c-66x7v | grep IP:

#Access the website from kubernetes cluster
curl http://10.233.84.73:5000

#Delete deployment
kubectl delete deployment webpod01