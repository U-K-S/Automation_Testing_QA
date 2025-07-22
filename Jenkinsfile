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
          "C:\\Users\\Utkarsh Kumar Singh\\anaconda3\\python.exe" -m pytest tests/ api_tests/ --html=report.html --self-contained-html

          REM Exit with test result status
          if ERRORLEVEL 1 exit /b 1
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true

      // Email the HTML report (requires Email Extension Plugin to be configured)
      emailext(
        to: 'utksh0308@gmail.com',
        subject: "🧪 Test Report: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
        body: """<p>Hello,</p>
<p>Please find attached the test report for <b>${env.JOB_NAME}</b> build #${env.BUILD_NUMBER}.</p>
<p>Thanks,<br>Jenkins</p>""",
        mimeType: 'text/html',
        attachmentsPattern: 'report.html'
      )
    }

    failure {
      echo '❌ Tests failed — see report.html in artifacts.'
    }

    success {
      echo '✅ All tests passed!'
    }
  }
}
