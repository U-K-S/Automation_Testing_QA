pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install & Test') {
      steps {
        // Run Windows batch commands under UTF‑8
        bat encoding: 'UTF-8', script: '''
          @echo off
          REM 1) Install pytest and HTML plugin
          python -m pip install --user --upgrade pytest pytest-html

          REM 2) Run tests and produce HTML report
          python -m pytest --html=report.html

          REM 3) Fail build on any test failures
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
      // Archive the HTML report so you can download/view it
      archiveArtifacts artifacts: 'report.html'
    }
    failure {
      echo 'Build failed because tests did not pass.'
    }
  }
}
