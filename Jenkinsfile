pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = 'sarvesh717'
        // We will use the build number as our image tag for versioning
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
        IMAGE_NAME = "${DOCKERHUB_USERNAME}/scientific-calculator"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                git branch: 'main', url: 'https://github.com/Sarvesh521/Scientific-Calculator-Mini-Project.git'                
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

        stage('5. Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i inventory deploy.yml'
            }
        }
    }
    post {
        success {
            mail to: 'sarveshkumara123@gmail.com',
                 subject: "SUCCESS: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                 body: "The pipeline run was successful. Check the build log here: ${env.BUILD_URL}"
        }
        failure {
            mail to: 'sarveshkumara123@gmail.com',
                 subject: "FAILURE: Pipeline '${env.JOB_NAME}' [${env.BUILD_NUMBER}]",
                 body: "The pipeline run failed. Check the build log for errors: ${env.BUILD_URL}"
        }
    }
}