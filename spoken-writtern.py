def get_rules():
    rules = {"Numbers":{
                        "zero": 0,
                        "one" : 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9,
                        "ten": 10,
                        "twenty": 20,
                        "thirty": 30,
                        "forty": 40,
                        "fifty": 50,
                        "sixty": 60,
                        "seventy": 70,
                        "eighty": 80,
                        "ninety": 90,
                        "hundred": 100
                        },
            "Tuples": {
                         "single":1,
                         "double":2,
                         "triple":3,
                         "quadruple":4,
                         "quintuple":5,
                         "sextuple":6,
                         "septuple":7,
                         "octuple":8,
                         "nonuple":9,
                         "decuple":10
                      },
            "General": {
                          "C M": "CM",
                          "P M": "PM",
                          "D M": "DM",
                          "A M": "AM"
                       }
            }
    return rules

def check_front_last(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last
        
def get_user_input():

    paragraph=input("Enter Your paragraph of spoken english:\n\t")

    if not paragraph:
        raise ValueError("[Error]: You entered nothing.")
    return paragraph


def Convert(paragraph):
    words_of_para=paragraph.split()
    
    rules = get_rules()
    numbers=rules['Numbers']
    tuples=rules['Tuples']
    general=rules['General']
    
    output_para = ""
    
    i=0
    no_of_words=len(words_of_para) 
    while i<no_of_words: 
        
        front,word,last=check_front_last(words_of_para[i])
        if i+1!= no_of_words:
            front_n,next_word,last_n=check_front_last(words_of_para[i+1])
            if word.lower() in numbers.keys() and (next_word.lower()=='dollars' or next_word.lower()=='dollar'):
                output_para+=" "+front+"$"+str(numbers[word.lower()])+last
                i=i+2

            elif word.lower() in tuples.keys() and len(next_word)==1:
                output_para += " "+front_n+(next_word*tuples[word.lower()])+last_n
                i=i+2
            elif (word+" "+next_word) in general.keys():
                output_para+=" "+front+word+next_word+last_n
                i=i+2
            else:
                output_para+=" "+words_of_para[i]
                i=i+1
        else:
            output_para+=" "+words_of_para[i]
            i=i+1
    return output_para

def convert_sp_to_wr():
    para = get_user_input()
    para = Convert(para)
    print("\nConverted Written English Paragraph: \n\n \"" +para+"\"")

if __name__ == "__main__":
    convert_sp_to_wr()