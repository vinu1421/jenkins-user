import hudson.model.*
import hudson.security.*

def userId = sathu
def password = sathu123

def instance = jenkins.model.Jenkins.instance

def existingUser = instance.securityRealm.allUsers.find {it.id == userId}
if (existingUser == null) {
    def user = instance.securityRealm.createAccount(userId, password)

} 