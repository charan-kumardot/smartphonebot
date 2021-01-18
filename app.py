from cht import Chat,reflections
from flask import Flask, render_template, request
from translate import Translator
translator= Translator(to_lang="Hebrew")


app = Flask(__name__, template_folder='templates')

pairs =[

        ['my name is (.*)| (.*)שמי',['hi %1 how can i help you?😊 choose the below optoions for the quire 1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['(hi|hello|hey|holla|היי|שלום)',['hey there how can i help you?😊 choose the below optoions for the quires 1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['(1|buy|לקנות את הסמארטפון|buy the smartphone📱|לִקְנוֹת)',['what type of smart phone do you want to buy?']],
        ['(2|למכור את הסמארטפון|מכירה|sell|sell the smartphone📱)',['what type of smart phone do you want to sell?']],
        ['(3|שֵׁרוּת|שירות לקוחות|service|customer service|customer)',['enter your number our manager will contact you soon']],
        ['(ACER|ALCATEL|ALLVIEW|AMAZONAMOI|APPLE|ARCHOS|ASUS|AT&T|BENEFON|BENQ|BENQ-SIEMENS|BIRD|BLACKBERRY|BLACKVIEW|BLUBOSCH|BQ|CASIO|CAT|CELKON|CHEA|COOLPAD|DELL|EMPORIA|ENERGIZER|ERICSSON|ETEN|FAIRPHONE|FUJITSU-SIEMENS|GARMIN-ASUS|GIGABYTE|GIONEE|GOOGLE|HAIER|HONOR|HPHTC|HUAWEI|I-MATE|I-MOBILE|ICEMOBILE|INFINIX|INQ|INTEX|JOLLA|KARBONN|KYOCERA|LAVA|LEECO|LENOVO|LG|MAXON|MAXWEST|MEIZU|MICROMAX|MICROSOFT|MITAC|MITSUBISHI|MODU|MOTOROLA|MWG|NEC|NEONODE|NIU|NOKIA|NVIDIA|ONEPLUS|OPPO|ORANGE|PALM|PANASONIC|PANTECH|PARLA|PHILIPS|PLUMPOSH|PRESTIGIO|QMOBILE|QTEK|RAZER|REALME|SAGEM|SAMSUNG|SENDO|SEWON|SHARP|SIEMENS|SONIM|SONY|SONY ERICSSON|SPICET-MOBILE|TCL|TECNO|TEL.ME.|TELIT|THURAYA|TOSHIBA|ULEFONE|UNNECTOVERT|UVERYKOOL|VIVO|VK MOBILE|VODAFONE|WIKO|WND|XCUTE|XIAOMI|XOLO|YEZZ|YOTA|YUZTE)',['enter your number our manager will contact you soon']],
        ['(4|אַחֵר|other|other quires)', ['choose the below optoions for the quires  1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['([\d{8,15}]|(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})|^(?:00|\\+)[0-9\\s.\\/-]{6,20}$)',['Thank you🤗.do you want to ask for other quires enter 4']],
        ['(quite|דַי|bye|QUITE|Bye|ביי)',['Thank you have a nice day.🤗']],
        ['(.*)', ['hey, choose the below optoions for the quires 1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']]
        ]

@app.route('/', methods=['GET', 'POST'])
def samplefunction():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        greetIn = request.form['human']
        greetOut = c(greetIn)
        return render_template('index.html',bot1=translator.translate(greetOut),bot2 = translator.translate(greetIn))


def c(x):
  chat = Chat(pairs,reflections)
  return chat.respond(x)







if __name__ == '__main__':
    app. run(host='127.0.4.21', port=4040, debug=True)






