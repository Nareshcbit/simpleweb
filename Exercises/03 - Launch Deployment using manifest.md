03 - Access POD from outside world

#Create Deployment
kubectl create -f deployment.yaml

#Get the list of deployments
kubectl get deployments
kubectl get deployments -o wide

#Get the list of pods
kubectl get pods

#Scaleup; Dont delete the existing instance
kubectl apply -f deployment.yaml

#Rollout new changes; replace the old instances with new instances


#Avaialability:Delete the Pod ( not deployment)
kubectl delete pod simpleweb-deployment-7c799f5769-tts4g
kubectl get pods
#can you see deployment created a new pod to maintain number of replicaes


#Update replicas ( either increase or decrease)
#Update the deployment
kubectl replace -f deployment.yaml
kubectl get pods

#Delete the deployment
kubectl delete -f deployment.yaml
kubectl get deployments
kubectl get pods

