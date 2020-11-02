pipeline {
    agent any


    stages{
        stage("Build") {
            steps {
                echo "开始构建..."
            }
        }
        stage("Test"){

             withPythonEnv("System-Cpython-3") {
                sh "pip3 install -r ./requirements.txt"
                // 进入该环境
                sh "source .pyenv-System-CPython-3/bin/activate"
             }

             steps {
                sh "pytest --cov=."
                echo "完成测试..."
             }
        }
        stage("Deploy")}{
            steps {
                echo "开始部署..."
            }
        }
    }
}