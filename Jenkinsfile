pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'study-cal'
        DOCKER_TAG = 'latest'
        // Replace with your Docker Hub username
        DOCKER_HUB_USERNAME = 'harishsagarla'
        // Use credentials configured in Jenkins
        DOCKER_HUB_CRED = credentials('docker-hub-credentials')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_HUB_USERNAME}/${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }
    }
    
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}