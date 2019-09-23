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
              sh "date=date +%s && git branch $date  ${rdtag} && git checkout $date"
              sh "git branch"
        }
    }



  }
}