import requests
import json

# set api key and project id
API_KEY = ""
PROJECT_ID = ''

# pull data from agilezen
URL = "https://agilezen.com/api/v1/projects/%s/stories/?apikey=%s&pageSize=1000&with=details,metrics,comments,tags" % (PROJECT_ID, API_KEY)

def get_stories():
  response = requests.get(URL, verify=False)  # turn off SSL certificates verification, not recommended
  dic = json.loads(response.text)
  return dic['items']
  
def process_story(story):
  item = {}
    
  item['objectID'] = "%s-%s" % (PROJECT_ID, story['id'])
  item['id'] = story['id']
  item['link'] = "https://agilezen.com/project/%s/story/%s" % (PROJECT_ID, story['id'])
  item['text'] = story['text']
  item['details'] = story['details']
  item['project'] = story['project']['name']
  item['color'] = story['color']
  item['priority'] = story['priority']
  item['phase'] = story['phase']['name']
  item['creator'] = story['creator']['name']
  item['createTime'] = story['metrics']['createTime']
  if 'owner' in story:
    item['owner'] = story['owner']['name']
  item['tags'] = [tag['name'] for tag in story['tags']]
  item['commentsCount'] = len(story['comments'])
  item['comments'] = [{'author': comment['author']['name'], 'createTime': comment['createTime'], 'text': comment['text']} for comment in story['comments']]
  
  # get attachment metadata
  item['attachments'] = process_attachment(story['id'])
  
  return item
  
def process_attachment(story_id):
  url = "https://agilezen.com/api/v1/projects/%s/stories/%s/attachments/?apikey=%s" % (PROJECT_ID, story_id, API_KEY)
  print(story_id)
  response = requests.get(url, verify=False)
  dic = json.loads(response.text)
  return [{'id': item['id'], 'name': item['fileName']} for item in dic['items']]
  
    
def save_file(list):
  with open('agilezen.json', 'w') as outfile:
    json.dump(list, outfile)
    

def main ():
  stories = get_stories()
  list = [process_story(story) for story in stories]
  save_file(list)

  
if __name__ == '__main__':
    main()
  

    