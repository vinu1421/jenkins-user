import hudson.model.*
import hudson.security.*

properties([
 [$class: 'JiraProjectProperty'],
 parameters([
 choice(choices: ['Donothing', 'Create_JenkinsUser', 'Reset_UserPassword', 'Update_JenkinsRoles', 'Update_JenkinsUsers'],
 description: 'Choose your action', name: 'ACTION'),
 string(defaultValue: '', description: 'Enter username', name: 'UserID', trim: false),
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
}

def managejenkins(String pAction, String pUserID, String pUsername){

    def password_generate(){
        def allChars = [ 'A'..'Z', 'a'..'z', '0'..'9' ].flatten() - [ 'O', '0', 'l', '1', 'I' ]
        def password = ""
        def generatePassword = { length ->
        (0..<length).collect { password = password + allChars[ new Random().nextInt( allChars.size() ) ] }
            }
        generatePassword(15)
        return password

    }

    node(){
        stage('ManageJenkins'){
            if (pAction == 'Create_JenkinsUser') {
                if (pUserID){
                    List user = pUserID.split(',')
                    def password = password_generate()
                    def instance = jenkins.model.Jenkins.instance
                    def existingUser = instance.securityRealm.allUsers.find {it.id == user[i]}
                    if (existingUser == null) {
                        echo "Creating user ${user[i]}"
                        def username = instance.securityRealm.createAccount(user[i], password)
                        if (pUsername) {
                            username.setFullName(pUsername)
                            }
                        echo "${user[i]} user created successfully, Password is ${password}"
                        } else {
                        echo "${user[i]} User already present in jenkins"
                        }
                    }
                } else {
                    echo "username is empty"

                }
                
            }
        }
    }
}

managejenkins("${ACTION}", "${UserID}", "${USERNAME}")
