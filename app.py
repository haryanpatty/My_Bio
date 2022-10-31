from flask import Flask 

app = Flask(__name__)

@app.get('/')
def userInfo():
    
    data = {'slackUsername':'Haryanpatty', 'backend':True, 'age':25, 'bio':'My name is Patience. I am a tech enthusiast'}
    return data
    
    
if __name__ =='__main__':
    

    app.run()
    
