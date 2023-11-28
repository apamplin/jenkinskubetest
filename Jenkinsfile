pipeline {

  agent {

    kubernetes {

      label 'my-kubernetes-agent'

    }
    docker {
        image 'node:20.10.0-alpine3.18'
        args '-p 3000:3000 -p 5000:5000' 
        }
    }

  

  

  stages {

    stage('Clone repository') {

      steps {

        git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/apamplin/jenkinskubetest.git'

      }

    }

    

    stage('Build and push Docker image') {

      steps {

        sh 'docker build -t my-image:latest .'

        sh 'docker tag my-image:latest localhost:32000/my-image:registry'

        sh 'docker push localhost:32000/my-image:registry'

      }

    }

    

    stage('Deploy to Kubernetes') {

      steps {

        kubernetesDeploy(

          configs: 'producepod.yaml'

        )

      }

    }

  }

}
