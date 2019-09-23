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
              sh "git fetch && git checkout ${rdtag}"
              sh "git branch"
        }
    }



  }
}