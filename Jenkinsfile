pipeline{
        agent any
        
        stages{
                stage('--Front End--'){
                        steps{
                                sh '''image="35.197.247.253:5000/frontend:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/frontend
                                      ssh 35.189.73.164  << EOF
                                      docker service update --image ${image} DnDCharacterGen_frontend
                                      '''
                        }
                }  
                stage('--Service1--'){
                        steps{
                                sh '''image="35.197.247.253:5000/rand1:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/randapp1
                                      ssh 35.197.247.253  << EOF
                                      docker service update --image ${image} DnDCharacterGen_service1
                                      '''
                        }
                }
                stage('--Service2--'){
                        steps{
                                sh '''image="35.197.247.253:5000/rand2:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/randapp2
                                      ssh 35.197.247.253  << EOF
                                      docker service update --image ${image} DnDCharacterGen_service2
                                      '''
                        }
                }
                stage('--Back End--'){
                        steps{
                                sh '''image="35.197.247.253:5000/backend:build-${BUILD_NUMBER}"
                                      docker build -t ${image} /var/lib/jenkins/workspace/DnD_master/backend
                                      ssh 35.197.247.253  << EOF
                                      docker service update --image ${image} DnDCharacterGen_backend
                                      '''
                        }
                }
                stage('--Clean up--'){
                        steps{
                                sh '''ssh 35.197.247.253  << EOF
                                      docker system prune
                                      '''
                        }
                }
        }
}
