pipeline {
    agent any
    stages{
        stage("Build") {
            steps {
                echo "开始构建..."
            }
        }
        stage("Test"){
            steps {
                withPythonEnv("System-CPython-3") {
                    sh "pip3 install -r ./requirements.txt"
                    // 进入该环境
                    sh "source .pyenv-System-CPython-3/bin/activate"
                    sh "pytest -vv testfile.py"
                    // 退出虚拟环境
                    sh "deactivate"
                    // 删除虚拟环境
                    sh "rm -rf .pyenv-System-CPython-3"
                }

                echo "完成测试..."
             }
        }
        stage("Deploy"){
            steps {
                echo "开始部署..."
            }
        }
    }
}
