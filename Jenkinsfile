pipeline {

  agent {

    kubernetes {

      label 'my-kubernetes-agent'

        }
    }

  stages {

    stage('Clone repository') {

      steps {

        git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/apamplin/jenkinskubetest.git'

      }

    }

    
    stage('Initialize Docker Tool'){

        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
        
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
