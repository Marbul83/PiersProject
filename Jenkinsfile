pipeline{
        agent any
        
        environment 
	{
		ssh_ip = "35.234.150.82"
	}
        
        stages{
                stage('--Front End--'){
                        steps{
                                sh '''image="35.234.148.125:5000/frontend:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/frontend
                                      docker push ${image}
                                      ssh 35.234.150.82  << EOF
                                      docker service update --image ${image} DnDCharacterGen_frontend
                                      EOF
                                      '''
                        }
                }  
                stage('--Service1--'){
                        steps{
                                sh '''image="35.234.148.125:5000/rand1:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/randapp1
                                      docker push ${image}
                                      ssh 35.234.150.82  << EOF
                                      docker service update --image ${image} DnDCharacterGen_service1
                                      EOF
                                      '''
                        }
                }
                stage('--Service2--'){
                        steps{
                                sh '''image="35.234.148.125:5000/rand2:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/randapp2
                                      docker push ${image}
                                      ssh 35.234.150.82  << EOF
                                      docker service update --image ${image} DnDCharacterGen_service2
                                      EOF
                                      '''
                        }
                }
                stage('--Back End--'){
                        steps{
                                sh '''image="35.234.148.125:5000/backend:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/backend
                                      docker push ${image}
                                      ssh 35.234.150.82  << EOF
                                      docker service update --image ${image} DnDCharacterGen_backend
                                      EOF
                                      '''
                        }
                }
        }
}
