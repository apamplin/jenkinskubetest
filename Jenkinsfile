pipeline {

  agent any

  stages {

    stage('Clone repository') {

      steps {

        git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/apamplin/jenkinskubetest.git'

      }

    }

    stage('Build and push Docker image') {
        agent {
            docker {
                label 'docker'
                image 'node:7-alpine'
            }
        }
      steps {

        sh 'docker build -t my-image:latest .'

        sh 'docker tag my-image:latest localhost:32000/my-image:registry'

        sh 'docker push localhost:32000/my-image:registry'

      }

    }

    

    stage('Deploy to Kubernetes') {

      steps {
        agent {
            label 'kubernetes'
        }

        kubernetesDeploy(

          configs: 'producepod.yaml'

        )

      }

    }

  }

}
