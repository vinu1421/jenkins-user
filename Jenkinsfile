import hudson.model.*
import hudson.security.*

properties([
    [$class: 'JiraProjectProperty'],
    
     parameters([

         [
            $class: 'ExtensibleChoiceParameterDefinition',
            choiceListProvider: [$class: 'TextareaChoiceListProvider',
            addEditedValue: false,
            choiceListText: '''Donothing\nUpdate_JenkinsRoles\nUpdate_JenkinsUsers''',
            defaultChoice: 'Donothing'],
            description: 'Choose an action to perform',
            editable: false,
            name: 'ACTION'
         ],
         string(defaultValue: '', description: 'Enter the username', name: 'USERNAME', trim: false)

         

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
'''
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
'''