from cht import Chat,reflections
from flask import Flask, render_template, request



app = Flask(__name__, template_folder='templates')

pairs =[

        ['my name is (.*)',['hi %1 how can i help you?😊 choose the below optoions for the quire 1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['(hi|hello|hey|holla)',['hey there how can i help you?😊 choose the below optoions for the quires 1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['(1|buy|buy the smartphone📱)',['what type of smart phone do you want to buy?']],
        ['(2|sell|sell the smartphone📱)',['what type of smart phone do you want to sell?']],
        ['(3|service|customer service|customer)',['enter your number our manager will contact you soon']],
        ['([a-zA-Z]+)',['enter your number our manager will contact you soon']],
        ['(4|other|other quires)', ['choose the below optoions for the quires  1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['([\d{8,15}]|([\d{8,15}]|(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})|^(?:00|\\+)[0-9\\s.\\/-]{6,20}$))',['Thank you🤗.do you want to ask for other quires enter 4']],
        ['(quite|bye|QUITE|Bye)',['Thank you have a nice day.🤗']]
        ]

@app.route('/', methods=['GET', 'POST'])
def samplefunction():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        greetIn = request.form['human']
        greetOut = c(greetIn)
        return render_template('index.html',bot1=greetOut,bot2 = greetIn)


def c(x):
  chat = Chat(pairs,reflections)
  return chat.respond(x)







if __name__ == '__main__':
    app. run(host='127.0.4.21', port=4040, debug=True)


