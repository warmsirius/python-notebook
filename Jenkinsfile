pipeline {
    agent any
    withPythonEnv("System-Cpython-3"){
    sh "pip3 install -r ./requirements.txt"
    // 进入该环境
    sh "source .pyenv-System-CPython-3/bin/activate"
    }

    stages{
        stage("Build") {
            echo "开始构建..."
        }
        stage("Test"){
            sh "pytest --cov=."
            echo "完成测试..."
        }
        stage("Deploy")}{
            echo "开始部署..."
        }
    }
}