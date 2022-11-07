from flask import Flask, Response, request
from db_instance import get_users

app = Flask(__name__)




@app.route('/')
def index():
  return "Hello world!"

@app.route('/users', methods=["GET"])
def users():

  all_users = get_users()
  args = request.args
  uid = args.get("uid")
  name = args.get("name")
  role = args.get("role")
  result = []

  if name is None:
            return all_users, 200
  elif name is not None:
    for doc in all_users:    
      for key, value in doc.items():
          if name==value:
            result.append(doc)
    return result, 200
    


if __name__ == '__main__':
  app.run()


