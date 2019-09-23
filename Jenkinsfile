pipeline {
  agent any
  stages {
    stage('as') {
      steps {
        build(job: 'aaa', propagate: true, wait: true)
      }
    }
  }
}