
capitals={'Alabama':'Montgomery','Alaska':'juneau','Arizona':'Phoenix','Arkansas':'Litlle Rock','California':'Scaramento',
'Colorado':'Denver','Conneticut':'Hartford','Delware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta',
'Hawaii':'Honolulu','Idaho':'Boise','Illinois':'SpringField','Indiana':'Indianapolis','Iowa':'Des Moines',
'Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta','Maryland':'Annapolis',
'Massachusetts':'Boston','Michigan':'Lansing','Minnesota':'Saint Paul','Mississippi':'Jackson','Misouri':'Jeffreson City',
'Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City','New Hampshire':'Concord','New Jersey':'Trenton',
'New Mexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh','North Dakota':'Bismarck','Ohio':'Colombus',
'Oklahoma':'Oklahoma City','Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia',
'South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier',
'Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston','Wisconsin':'Madison','Wyoming':'Cheyenne'}

for i in range(35):
    myquesfile=open(f"!quizquesform{i+1}.txt","w")
    myquesfile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    myquesfile.write(f"\n\nState Capitals Quiz (Form{i})\n\n\n")
    import random
    states = list(capitals.keys())
    random.shuffle(states)
    answerKeyFile = open(f'!quizanswersform{i + 1}.txt', "w")

    for quesnum in range(len(capitals)):

        correctans = capitals[states[quesnum]]
        wrongans=list(capitals.values())
        del wrongans[wrongans.index(correctans)]
        wrongans=random.sample(wrongans,3)
        answeroptions=wrongans+[correctans]
        random.shuffle(answeroptions)

        myquesfile.write(f"{quesnum+1}. What is the capital of {states[quesnum]}?\n\n")
        for i in range(4):
            myquesfile.write(f"     {'ABCD'[i]}.{answeroptions[i]}\n")
        myquesfile.write("\n")

        answerKeyFile.write(f'{quesnum+1}.{"ABCD"[answeroptions.index(correctans)]}\n\n\n')


    myquesfile.close()
    answerKeyFile.close()