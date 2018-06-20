03 - Access POD from outside world

#Create Deployment
kubectl create -f deployment.yaml

#Get the list of deployments
kubectl get deployments
kubectl get deployments -o wide

#Get the list of pods
kubectl get pods

#Delete the Pod ( not deployment)
kubectl delete pod simpleweb-deployment-7c799f5769-tts4g

#Wait for few seconds and run
kubectl get pods
#can you see deployment created a new pod to maintain number of replicaes


#Update replicas ( either increase or decrease)
#Update the deployment
kubectl replace -f deployment.yaml

