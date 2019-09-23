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
              sh "git branch"
              sh "git status"

              sh "git checkout . && git fetch && git pull && git checkout ${rdtag}"
              sh "git branch"
        }
    }



  }
}