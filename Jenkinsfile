pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code from the repository
                // Replace the repository URL and credentials as needed
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Build your project
                // Replace with your build commands or scripts
                git 'https://github.com/samvb007/test.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                // Run SonarQube analysis
                withSonarQubeEnv('SonarQube Server') {
                    // Replace with your SonarQube project key and name
                    sh 'mvn sonar:sonar -Dsonar.projectKey=my-project -Dsonar.projectName=MyProject'
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy your project
                // Replace with your deployment commands or scripts
                sh 'echo "Deploying..."'
            }
        }
    }

    post {
        always {
            // Publish SonarQube results as a build step
            // Replace with your SonarQube server URL and authentication token
            script {
                def scannerHome = tool 'SonarQube Scanner'
                withSonarQubeEnv('SonarQube Server') {
                    def scan = scannerHome + '/bin/sonar-scanner'
                    sh "${scan} -Dsonar.login=<sonarqube_token>"
                }
            }
        }
    }
}
