pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = 'your-dockerhub-username'
        // We will use the build number as our image tag for versioning
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/scientific-calculator"
    }
    stages {
        stage('1. Checkout') { steps { checkout scm } }
        stage('2. Test') {
            steps {
                script {
                    docker.image('python:3.9-slim-buster').inside {
                       sh 'python -m unittest discover'
                    }
                }
            }
        }
        stage('3. Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${IMAGE_TAG}", '.')
                }
            }
        }
        stage('4. Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                        // Also tag this build as the 'latest'
                        docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push('latest')
                    }
                }
            }
        }
    }
}