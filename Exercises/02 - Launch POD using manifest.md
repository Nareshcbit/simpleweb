02 - Launch POD using manifest.md

#Launch POD
kubectl create -f pod.yaml

#Get the list of deployments - can you see deployments? 
kubectl get deployments 
kubectl get deployments -o wide
#Note: Check the manifest and see 'kind'


#Get the list of pods
kubectl get pods
kubectl get pods -o wide 

#record pod ip
kubectl get pods -o wide 
kubectl describe pod simple | grep IP:

#Access the website from kubernetes cluster
curl http://10.233.122.139:5000
#Question? is output different from what we got in exercise1? see simpleweb.py 


#Delete pod
kubectl delete pod simpleweb
