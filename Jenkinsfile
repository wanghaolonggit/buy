pipeline {
  agent any
  parameters {

    string(
        description: '后端 Tag',
        name: 'rdtag',
        defaultValue: 'master',
    )

  }

  stages {


    stage('Prepare') {
        steps {
              echo "build_tag: ${rdtag}"
              sh "git chechout ${rdtag}"
              sh "git branch"
        }
    }



  }
}