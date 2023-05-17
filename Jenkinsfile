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
                    $env:SONAR_SCANNER_VERSION = "4.7.0.2747"
                    $env:SONAR_DIRECTORY = [System.IO.Path]::Combine($(get-location).Path,".sonar")
                    $env:SONAR_SCANNER_HOME = "$env:SONAR_DIRECTORY/sonar-scanner-$env:SONAR_SCANNER_VERSION-windows"
                    rm $env:SONAR_SCANNER_HOME -Force -Recurse -ErrorAction SilentlyContinue
                    New-Item -path $env:SONAR_SCANNER_HOME -type directory
                    (New-Object System.Net.WebClient).DownloadFile("https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-$env:SONAR_SCANNER_VERSION-windows.zip", "$env:SONAR_DIRECTORY/sonar-scanner.zip")
                    Add-Type -AssemblyName System.IO.Compression.FileSystem
                    [System.IO.Compression.ZipFile]::ExtractToDirectory("$env:SONAR_DIRECTORY/sonar-scanner.zip", "$env:SONAR_DIRECTORY")
                    rm ./.sonar/sonar-scanner.zip -Force -ErrorAction SilentlyContinue
                    $env:Path += ";$env:SONAR_SCANNER_HOME/bin"
                    $env:SONAR_SCANNER_OPTS="-server"
                }
            }
    
    }
}
