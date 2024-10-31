pipeline {
    agent any

    parameters {
        string(name: 'NUMBER1', defaultValue: '0', description: 'First number to add')
        string(name: 'NUMBER2', defaultValue: '0', description: 'Second number to add')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Setting up Python environment...'
                // Set up Python environment (optional)
                bat 'python3 -m venv venv'
                bat '. venv/bin/activate'                
            }
        }
        stage('Execute') {
            steps {
                echo 'Running Python script...'
                // Run the Python script with the parameters
                bat "python3 sum.py ${params.NUMBER1} ${params.NUMBER2}"
            }
        }
    }    
}
