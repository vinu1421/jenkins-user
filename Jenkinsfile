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
         ]    

         

    ])    
]) 
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