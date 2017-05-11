import requests
import json

# set user name and password for agilezen login
USERNAME = ""
PASSWORD = ""

LOGIN_URL = "https://agilezen.com/login"

# set project id
PROJECT_ID = ''

def login():
  session = requests.session()

  # Create payload
  payload = {
      "userName": USERNAME, 
      "password": PASSWORD
  }

  # Perform login
  response = session.post(LOGIN_URL, data = payload, verify=False)
  
  return session

def main():
  session = login()
    
  # change file name
  with open('agilezen.json') as json_data:
    stories = json.load(json_data)

  for story in stories:
    for attachment in story['attachments']:
      print(story['id'])
      url = "https://agilezen.com/project/%s/story/%s/attachment/%s/download/%s" % (PROJECT_ID, story['id'], attachment['id'], attachment['name'])
      response = session.get(url, verify=False)
      file_name = "%s_%s" % (attachment['id'], attachment['name'])
      with open(file_name, 'wb') as outfile:
        outfile.write(response.content)
    
if __name__ == '__main__':
  main()
    
    
   
  