pipeline{
        agent any
        
        environment 
	{
		ssh_ip = "35.234.150.82"
	}
        
        stages{
                stage('--Front End--'){
                        steps{
                                sh '''image="jenkins:5000/frontend:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /frontend
                                      docker push ${image}
                                      gcloud compute ssh swarm-master --zone europe-west2-c  << EOF
                                      docker service update --image ${image} DnDCharacterGen_frontend
                                      EOF
                                      '''
                        }
                }  
                stage('--Service1--'){
                        steps{
                                sh '''image="jenkins:5000/rand1:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /randapp1
                                      docker push ${image}
                                      gcloud compute ssh swarm-master --zone europe-west2-c  << EOF
                                      docker service update --image ${image} DnDCharacterGen_service1
                                      EOF
                                      '''
                        }
                }
                stage('--Service2--'){
                        steps{
                                sh '''image="jenkins:5000/rand2:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /randapp2
                                      docker push ${image}
                                      gcloud compute ssh swarm-master --zone europe-west2-c  << EOF
                                      docker service update --image ${image} DnDCharacterGen_service2
                                      EOF
                                      '''
                        }
                }
                stage('--Back End--'){
                        steps{
                                sh '''image="jenkins:5000/backend:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /backend
                                      docker push ${image}
                                      gcloud compute ssh swarm-master --zone europe-west2-c  << EOF
                                      docker service update --image ${image} DnDCharacterGen_backend
                                      EOF
                                      '''
                        }
                }
        }
}
