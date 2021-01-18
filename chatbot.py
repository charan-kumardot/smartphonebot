from cht import Chat,reflections
pairs =[

        ['my name is (.*)',['hi %1 how can i help you? choose the below optoions for the quire 1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['(hi|hello|hey|holla)',['hey there how can i help you? choose the below optoions for the quires /n 1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['(1|buy|buy the smartphone)',['what type of smart phone do you want to buy?']],
        ['(2|sell|sell the smartphone)',['what type of smart phone do you want to sell?']],
        ['(3|service|customer service|customer)',['enter your number our manager will contact you soon']],
        ['([a-zA-Z]+)',['enter your number our manager will contact you soon']],
        ['(4|other|other quires)', ['choose the below optoions for the quires  1.for buy a smartphone(enter 1) 2.for sell the smartphone(enter 2) 3.for customer service(enter 3)']],
        ['([\d{8,15}])',['Thank you.do you want to ask for other quires enter 4']],
        ['(quite|bye|QUITE|Bye)',['Thank you have a nice day.']]
        ]


Chat = Chat(pairs, reflections)
response = Chat.converse()

