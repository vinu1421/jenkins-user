import hudson.model.*
import hudson.security.*

properties([
 [$class: 'JiraProjectProperty'],
 parameters([
 choice(choices: ['Donothing', 'Create_JenkinsUser', 'Reset_UserPassword', 'Update_JenkinsRoles', 'Update_JenkinsUsers'],
 description: 'Choose your action', name: 'ACTION'),
 string(defaultValue: '', description: 'Enter username', name: 'USERNAME', trim: false)
 ])
])

def checkoutRepo(){

	stage('Checkout Repo') {
		checkout([$class: 'GitSCM', 
        branches: [[name: '*/script-branch']], 
        doGenerateSubmoduleConfigurations: false, 
        extensions: [], 
        submoduleCfg: [], 
        userRemoteConfigs: [[credentialsId: '918483d2-a278-43f7-8618-1dc618466dfc', url: 'https://github.com/vinu1421/jenkins-user.git']]
        
        ])
	}

def userId = 'sathu'
def password = 'sathu123'
def fullname = 'sathvik vinayak'

def instance = jenkins.model.Jenkins.instance

def existingUser = instance.securityRealm.allUsers.find {it.id == userId}
if (existingUser == null) {
    def user = instance.securityRealm.createAccount(userId, password)
    user.setFullName(fullname)
    echo 'user created successfully'

} else {
    echo 'User already present'
}
