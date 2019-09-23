pipeline {
  agent any

  stages {
    stage('Prepare') {
        steps {
                echo "build_tag: ${params.environment}"
             }
    }

    stage('Prepare') {
        steps {
              echo "build_tag: ${params.environment}"
              sh "git branch date +%s  ${rdtag}"
        }
    }

}