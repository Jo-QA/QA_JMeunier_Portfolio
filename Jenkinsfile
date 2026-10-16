// Linux agent: Python 3.12 + Chrome + network to public demo and driver distribution.
pipeline {
    agent { label 'qa-python312-chrome' }
    options { timestamps(); timeout(time: 15, unit: 'MINUTES'); disableConcurrentBuilds() }
    environment { SD_HEADLESS = 'true'; SE_AVOID_STATS = 'true'; TZ = 'UTC' }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Install') { steps {
            sh 'python3.12 -m venv .venv'
            sh '.venv/bin/python -m pip install -r requirements.txt'
            sh '.venv/bin/python -m pip check'
        } }
        stage('Validate') { steps {
            sh '.venv/bin/python scripts/validate_portfolio.py'
            sh '.venv/bin/python -m unittest discover -s tests/unit -v'
        } }
        stage('UI regression') { steps {
            sh '.venv/bin/python scripts/run.py --suite regression --output results/jenkins-${BUILD_NUMBER}'
        } }
    }
    post {
        always {
            sh 'if [ -f results/jenkins-${BUILD_NUMBER}/environment.json ]; then .venv/bin/python scripts/summarize.py results/jenkins-${BUILD_NUMBER}; fi'
            junit testResults: "results/jenkins-${env.BUILD_NUMBER}/xunit.xml", allowEmptyResults: true
            archiveArtifacts artifacts: "results/jenkins-${env.BUILD_NUMBER}/**", allowEmptyArchive: true
        }
    }
}
