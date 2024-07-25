pipeline {
    agent any

    parameters {
        string(name: 'NUMBER1', defaultValue: '0', description: 'First number to add')
        string(name: 'NUMBER2', defaultValue: '0', description: 'Second number to add')
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git 'https://github.com/tu-usuario/tu-repositorio.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Setting up Python environment...'
                // Set up Python environment (optional)
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
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
