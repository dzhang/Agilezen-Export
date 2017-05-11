# Agilezen-Export
export Agilezen data through API with python

archive.py
export Agilezen stories, comments, tags, and attachment metadata (not the attachment itself)
save the data into local file named agilezen.json
make sure you set api_key and project id at the top of the script

attachment.py
go through each story, and download the attachment itself to local
make sure you set Agilezen login and project id at the top of the script

Once you have the data in agilezen.json, you can upload it to Algolia.com
