pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Test') {
      steps {
        bat encoding: 'UTF-8', script: '''
          @echo off
          REM Run tests and generate HTML report
          "C:\\Users\\Utkarsh Kumar Singh\\anaconda3\\python.exe" -m pytest --html=report.html

          REM Fail build if tests failed
          if ERRORLEVEL 1 exit /b 1
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'report.html'
    }
    failure {
      echo 'Tests failed—see report.html'
    }
  }
}
