import groovy.json.JsonOutput
/**
 * Executes a curl command with the specified method, url, payload, and jq filter.
 *
 * @param method The HTTP method to use (e.g., 'GET', 'POST', 'PATCH')
 * @param url The URL to send the request to
 * @param data The payload to send with the request (optional)
 * @param jqFilter The jq filter to apply to the response (optional)
 */
def executeCurlCommand(String method, String url, String data, String jqFilter) {
    def command = """
        curl -L \\
        -X ${method} \\
        -H "Accept: application/vnd.github+json" \\
        -H "Authorization: Bearer \$GIT_PASSWORD" \\
        -H "X-GitHub-Api-Version: 2022-11-28" \\
        '${url}' \\
        ${data ? "-d '${data}'" : ""}
    """

    def response = sh(script: command, returnStdout: true).trim()

    if (jqFilter) {
        response = sh(script: "echo '${response}' | jq -r '${jqFilter}'", returnStdout: true).trim()
    }

    return response
}
pipeline {
    agent {
        docker {
            image 'docker:24.0.2'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    }
    triggers {
        pollSCM('H/5 * * * *') // Poll the repository every 5 minutes
    }
    stages {
        stage('Pre-Build') {
            steps {
                container('docker') {
                    sh '''
                        apk add curl jq
                        echo "Pull Request Branch: ${env.CHANGE_BRANCH}"
                        echo "env contains: ${JsonOutput.toJson(env)}"
                        echo "Contents of README.md:"
                        cat README.md
                    '''
                }
            }
        }
        stage('Build and Test') {
            steps {
                script {
                    try {
                        sh 'mvn clean test'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                def status = currentBuild.result == 'SUCCESS' ? 'success' : 'failure'
                def message = currentBuild.result == 'SUCCESS' ? 'All tests passed!' : 'Some tests failed.'
                def context = 'continuous-integration/jenkins'
                
                // Post status to GitHub
                def commitSha = env.GIT_COMMIT
                echo "Commit SHA: ${commitSha}"
                def repoName = env.GIT_URL.tokenize('/').last().replace('.git', '')
                echo "Repo Name: ${repoName}"
                def repoOwner = env.GIT_URL.tokenize('/')[-2]
                echo "Repo Owner: ${repoOwner}"
                def githubToken = credentials('github-login')

                withCredentials([string(credentialsId: 'github-login', variable: 'GITHUB_TOKEN')]) {
                    sh """
                        curl -H "Authorization: token ${GITHUB_TOKEN}" \
                             -H "Content-Type: application/json" \
                             -X POST \
                             -d '{
                                   "state": "${status}",
                                   "target_url": "${env.BUILD_URL}",
                                   "description": "${message}",
                                   "context": "${context}"
                                 }' \
                             https://api.github.com/repos/${repoOwner}/${repoName}/statuses/${commitSha}
                    """
                }
            }
        }
    }
}