pipeline {
    agent { docker { image 'python:3.9-slim' } }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository configured in the job
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                // Run pytest and produce a JUnit XML so Jenkins can display results
                sh 'pytest -q --junitxml=reports/results.xml'
            }
        }
    }

    post {
        always {
            // Archive test results (will be visible in Jenkins UI)
            archiveArtifacts artifacts: 'reports/results.xml', allowEmptyArchive: true
            junit 'reports/results.xml'
        }

        success {
            echo 'Tests passed — pipeline successful.'
        }

        failure {
            echo 'One or more tests failed. See Console Output and test report.'
        }
    }
}