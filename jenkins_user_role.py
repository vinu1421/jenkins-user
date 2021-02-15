#!/usr/bin/env python3
import os
from pyjars import RoleStrategy, permission, Role
import json



user_file = open("./jenkins_user.json", "r")
role_file = open("./jenkins_roles.json", "r")
jenkins_role = json.load(role_file)
jenkins_user = json.load(user_file)
user_file.close()
role_file.close()

action = os.getenv("ACTION")
rs = RoleStrategy('http://localhost:8080', 'vi1421', 'bigf1shvi1421', ssl_verify=False, ssl_cert=None)



def user_manage(position, function):

    for data in jenkins_user[position]:
     relm = data['relm']
     roles = list(data['roles'].keys())
     for role_names in roles:
      userlist = data['roles'][role_names]
      for users in userlist:
       builder_role = Role(rs, relm, role_names)
       if function == 'assign':
        response = builder_role.assign_sid(users)
       elif function == 'unassign':
        response = builder_role.unassign_sid(users)
       if response.status_code == 200:
        print(function+ ' of role '+role_names+ ' to the user ' +users+ ' is successful')
       else:
        print('Failed to '+function+' role '+role_names+ ' to the user ' +users)


def remove_jenkinsrole():
    
    for data in jenkins_role['absent']:
        role_name = data['name']
        relm = data['relm']
        builder_role = Role(rs, relm, role_name)
        response = builder_role.delete()
        if response.status_code == 200:
            print(role_name+ ' in ' +relm+ ' deleted successfully')
        else:
            print(role_name+' in '+relm+ 'Failed to delete role')
    
def add_jenkinsrole():
    for data in jenkins_role['present']:
        role_name = data['name']
        pattern_name = data['pattern']
        relm = data['relm']
        job_permission = list(data['role'].keys())
        if job_permission:
            new_role = Role(rs, relm, role_name)
            role_counter = []
            for items in job_permission:
                    role_value = list(data['role'][items].keys())
                    if items == 'Agent':
                     items = permission.AgentPermission()
                    elif items == 'Overall':
                     items = permission.OverallPermission()
                    elif items == 'Job':
                     items = permission.JobPermission()
                    elif items == 'Credentials':
                     items = permission.CredentialPermission()
                    elif items == 'Run':
                     items = permission.RunPermission()
                    elif items == 'View':
                     items = permission.ViewPermission()
                    elif items == 'SCM':
                     items = permission.ScmPermission()
                    for keys in role_value:
                        setattr(items, keys, True)
                    role_counter.append(items)
            
            new_role.add_permission(role_counter)
            response = new_role.create(pattern=pattern_name)
            if response.status_code == 200:
                print(role_name+' role created/updated successfully')
            else:
                print(role_name+' role creation/updation failed')


if action == 'Update_JenkinsRoles':
    if jenkins_role['present']:
      print('Updating Jenkins roles')
      add_jenkinsrole()
    else:
      print('no roles to create/update from jenkins')

    if jenkins_role['absent']:
      print('Removing jenkins roles')
      remove_jenkinsrole()
    else:
      print('no roles to remove from jenkins')

elif action == 'Update_JenkinsUsers':
    if jenkins_user['present']:
      print('Updating all jenkins users to corresponding roles')
      user_manage('present', 'assign')
    else:
      print('No user to assign roles')

    if jenkins_user['absent']:
      print('Removing roles assigned to users')
      user_manage('absent', 'unassign')
    else:
      print('No user to unassign roles')
else:
    print('No action selected')

