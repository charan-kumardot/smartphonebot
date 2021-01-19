from cht import Chat,reflections
from flask import Flask, render_template, request
from twilio.twiml.messaging_response import MessagingResponse




app = Flask(__name__, template_folder='templates')

pairs =[
        ['(1)',['באיזה מכשיר אתם מתעניינים?']],
        ['(2)',['''
        לקוח יקר אם ברשותך מערכת סינון והגנה מבית מושגח פלוס
 נא לפנות בכל פנייה לגבי חנות האפליקציות, להוסיף אפליקציה להגביר רמת סינון וכו'... 
 אל מוקד שירות לקוחות אפליקצית מושגח 
בימים א-ה בין השעות 10:00-17:00 : 058-3777779
ניתן גם לפנות אלינו(מומלץ) גם במייל: mp058377@gmail.com

לקוח נכבד, אם ברשותך מערכת סינון והגנה מבית כושר פליי
נא לפנות בכל פנייה לגבי חנות האפליקציות, להוסיף אפליקציה להגביר רמת סינון וכו'... 
אל מוקד שירות לקוחות ווטסאפ (לוחצים על המעטפה) 
אפליקצית כושר פליי ‏‪053-312-3889‬‏
ניתן גם לפנות אלינו(מומלץ) גם במייל: kosherplay@gmail.com
נא לשמור על הקופסא ושטר האחריות
תקשורת טובה היא שם המשחק תרגישו חופשי לשתף אותנו 
תשאלו תבררו אנחנו כאן לעזור לכם… במייל ובטלפון איך שנוח לכם.
        ''']],
        ['(3)',['רשום בבקשה את מספר הטלפון שלך ונציג יחזור אליך בהקדם']],
        ['(ACER|ALCATEL|ALLVIEW|AMAZONAMOI|APPLE|ARCHOS|ASUS|AT&T|BENEFON|BENQ|BENQ-SIEMENS|BIRD|BLACKBERRY|BLACKVIEW|BLUBOSCH|BQ|CASIO|CAT|CELKON|CHEA|COOLPAD|DELL|EMPORIA|ENERGIZER|ERICSSON|ETEN|FAIRPHONE|FUJITSU-SIEMENS|GARMIN-ASUS|GIGABYTE|GIONEE|GOOGLE|HAIER|HONOR|HPHTC|HUAWEI|I-MATE|I-MOBILE|ICEMOBILE|INFINIX|INQ|INTEX|JOLLA|KARBONN|KYOCERA|LAVA|LEECO|LENOVO|LG|MAXON|MAXWEST|MEIZU|MICROMAX|MICROSOFT|MITAC|MITSUBISHI|MODU|MOTOROLA|MWG|NEC|NEONODE|NIU|NOKIA|NVIDIA|ONEPLUS|OPPO|ORANGE|PALM|PANASONIC|PANTECH|PARLA|PHILIPS|PLUMPOSH|PRESTIGIO|QMOBILE|QTEK|RAZER|REALME|SAGEM|SAMSUNG|SENDO|SEWON|SHARP|SIEMENS|SONIM|SONY|SONY ERICSSON|SPICET-MOBILE|TCL|TECNO|TEL.ME.|TELIT|THURAYA|TOSHIBA|ULEFONE|UNNECTOVERT|UVERYKOOL|VIVO|VK MOBILE|VODAFONE|WIKO|WND|XCUTE|XIAOMI|XOLO|YEZZ|YOTA|YUZTE|וואן פלוס|סמסונג|שיאומי)',['רשום בבקשה את מספר הטלפון שלך ונציג יחזור אליך בהקדם']],
        ['([\d{8,15}]|(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})|^(?:00|\\+)[0-9\\s.\\/-]{6,20}$)',['תודה רבה מצוות המגן סלולרי בהשגחה פרטית']],
        ['(.*)',['''ברוכים הבאים למגן סלולרי בהשגחה פרטית, איך אפשר לעזור? 
        לעזרה ברכישת מכשיר לחץ 1
לעזרה בנושאי שירות לקוחות לחץ 2
תרצו לדבר עם מנהל מכירות לחץ 3''']]
]





@app.route('/', methods=['GET', 'POST'])
def samplefunction():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        greetIn = request.form['human']
        greetOut = c(greetIn)
        return render_template('index.html',bot1 = greetOut,bot2 = greetIn)


def c(x):
  chat = Chat(pairs,reflections)
  return chat.respond(x)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming with a simple text message."""
    resp = MessagingResponse()
    phoneno = request.form.get('From')
    msg = request.form.get('Body')
    chat = Chat(pairs, reflections)

    print(msg)
    resp.message(chat.respond(msg))
    return str(resp)






if __name__ == '__main__':
    app. run(host='127.0.4.21', port=4040)
















