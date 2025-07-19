pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Prepare & Test') {
      steps {
        bat encoding: 'UTF-8', script: '''
          @echo off
          REM — If venv doesn’t exist, create it and install only once
          if not exist venv (
            echo Creating virtualenv…
            "C:\\Users\\Utkarsh Kumar Singh\\anaconda3\\python.exe" -m venv venv
            call venv\\Scripts\\activate
            python -m pip install --upgrade pip
            python -m pip install pytest pytest-html pytest-cov
          ) else (
            echo Reusing existing virtualenv…
            call venv\\Scripts\\activate
          )

          REM — Run tests with HTML, JUnit and coverage reports
          python -m pytest ^
            --html=report.html ^
            --junitxml=junit.xml ^
            --cov=my_package --cov-report=xml:coverage.xml

          REM — Fail the build if tests fail
          if ERRORLEVEL 1 exit /b 1
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'report.html'
      junit 'junit.xml'
      publishCoverage adapters: [coberturaAdapter('coverage.xml')]
    }
    failure {
      echo 'Build failed—see reports above.'
    }
  }
}
