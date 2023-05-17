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
                git branch : 'master' , url:'https://github.com/samvb007/test.git'
            }
        }

        stage('SonarQube Scan') 
            steps {
                // Run SonarQube analysis
                withSonarQubeEnv('sonarserver') {
                    // Replace with your SonarQube project key and name
                      sonar-scanner.bat -D"sonar.projectKey=sonar-key" -D"sonar.sources=." -D"sonar.host.url=http://127.0.0.1:9000
            }
         }    
    }
}
