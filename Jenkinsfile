pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = 'sarvesh717'
        // We will use the build number as our image tag for versioning
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/scientific-calculator"
    }
    stages {
        stage('1. Checkout') { 
            steps { 
                checkout scm 
            } 
        }
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
    // --- ADD THIS ENTIRE POST SECTION ---
    post {
        success {
            // This block runs only if the pipeline is successful
            mail to: 'sarveshkumara123@gmail.com',
                 subject: "SUCCESS: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                 body: "The pipeline run was successful. Check the build log here: ${env.BUILD_URL}"
        }
        failure {
            // This block runs only if the pipeline fails
            mail to: 'sarveshkumara123@gmail.com',
                 subject: "FAILURE: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                 body: "The pipeline run failed. Check the build log for errors: ${env.BUILD_URL}"
        }
    }
}