pipeline {
    agent any
    
    stages {
        stage('Cloning from git') {
            steps {
                git branch: 'master', url: 'https://github.com/Muhammad-Saad12/mlops-task3'
            }
        }

        stage('Installation of dependencies') {
            steps {
                bat 'C:\WINDOWS\system32\cmd.exe pip3 install -r requirement.txt'
                echo 'Dependencies successfully installed!'
            }
        }

        stage('Test') {
            steps {
                bat 'python test.py'
                echo 'Tests passed!'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'master') {
                        echo 'Deploying to production...'
                    } else {
                        echo 'Deploying to development server...'
                    }
                }
            }
        }
    }
}
