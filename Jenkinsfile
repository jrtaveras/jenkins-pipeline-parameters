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
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt' // If you have dependencies
            }
        }
        stage('Execute') {
            steps {
                echo 'Running Python script...'
                // Run the Python script with the parameters
                sh "python3 sum.py ${params.NUMBER1} ${params.NUMBER2}"
            }
        }
    }    
}
