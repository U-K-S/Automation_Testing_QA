pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Test') {
      steps {
        bat '''
          @echo off
          echo Running pytest and generating HTML report...

          REM Run tests and generate HTML report
          "C:\\Users\\Utkarsh Kumar Singh\\anaconda3\\python.exe" -m pytest tests/ --html=report.html --self-contained-html

          REM Exit with test result status
          if ERRORLEVEL 1 exit /b 1
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
    }
    failure {
      echo '❌ Tests failed — see report.html in artifacts.'
    }
    success {
      echo '✅ All tests passed!'
    }
  }
}
