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
                                      cd /PiersProject/frontend
                                      docker build -t ${image}
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
                                      cd /PiersProject/randapp1
                                      docker build -t ${image}
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
                                      cd /PiersProject/randapp2
                                      docker build -t ${image}
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
                                      cd /PiersProject/backend
                                      docker build -t ${image}
                                      docker push ${image}
                                      gcloud compute ssh swarm-master --zone europe-west2-c  << EOF
                                      docker service update --image ${image} DnDCharacterGen_backend
                                      EOF
                                      '''
                        }
                }
        }
}
