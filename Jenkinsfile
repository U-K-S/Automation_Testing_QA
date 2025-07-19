pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps { checkout scm }
    }

    stage('Prepare & Test') {
      steps {
        bat encoding: 'UTF-8', script: '''
          @echo off
          REM — If venv doesn’t exist, create it and install once
          if not exist venv (
            echo Creating virtualenv…
            "C:\\Users\\Utkarsh Kumar Singh\\anaconda3\\python.exe" -m venv venv
            call venv\\Scripts\\activate

            REM — Upgrade pip and install all test dependencies
            python -m pip install --upgrade pip
            python -m pip install pytest pytest-html pytest-cov selenium
          ) else (
            echo Activating existing virtualenv…
            call venv\\Scripts\\activate
          )

          REM — Run pytest, generate HTML, JUnit XML, and coverage XML
          python -m pytest ^
            --html=report.html ^
            --junitxml=junit.xml ^
            --cov=my_package --cov-report=xml:coverage.xml

          REM — Fail the build if any tests fail
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
      echo 'Build failed—see report.html and junit.xml for details.'
    }
  }
  
