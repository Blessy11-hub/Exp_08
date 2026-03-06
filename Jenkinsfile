pipeline {
    agent any
    parameters {
        string(name: 'APP_NAME', defaultValue: 'MyTerminalApp', description: 'Enter App Name')
        string(name: 'VERSION', defaultValue: '1.0', description: 'Enter Version')
    }
    stages {
        stage('Checkout') {
            steps {
                // This checks out the code from the repo configured in Jenkins
                checkout scm
            }
        }
        stage('Process Parameters') {
            steps {
                // Task 2: Display all values
                echo "Application: ${params.APP_NAME}"
                echo "Version: ${params.VERSION}"
                
                // Task 3: Store in parameters.txt
                sh "echo 'App: ${params.APP_NAME}, Ver: ${params.VERSION}' > parameters.txt"
            }
        }
    }
}