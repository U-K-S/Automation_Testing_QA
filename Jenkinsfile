pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Install & Test') {
      steps {
        bat encoding: 'UTF-8', script: '''
          @echo off
          REM — use full path to your Anaconda Python
          "C:\\Users\\Utkarsh Kumar Singh\\anaconda3\\python.exe" -m pip install --user --upgrade pytest pytest-html

          REM — run pytest via that same interpreter
          "C:\\Users\\Utkarsh Kumar Singh\\anaconda3\\python.exe" -m pytest --html=report.html

          REM — fail build if any tests fail
          if ERRORLEVEL 1 (
            echo ERROR: Some tests failed
            exit /b 1
          ) else (
            echo All tests passed.
          )
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'report.html'
    }
    failure {
      echo 'Build failed—check report.html'
    }
  }
}
