import json
import re

def doesHaveLinks(sms):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    result = [x[0] for x in re.findall(regex, sms)]
    return len(result) > 0
    
def doesHaveSpammyWords(sms):
    spammy_words = ['call', 'free', 'mobile', 'claim', 'reply', 'contact', 'stop', 'won', 'prize', 'cash']
    for word in spammy_words:
        if word in sms:
            return True
    return False
    
def getlengthOfText(sms):
    return len(sms)

def makePrediction(sms):
    hasLinks = doesHaveLinks(sms)
    hasSpammyWords = doesHaveSpammyWords(sms)
    lengthOfText = getlengthOfText(sms)
    if lengthOfText > 97:
        if hasSpammyWords:
            if lengthOfText > 183:
                return 'ham'
            else:
                if lengthOfText > 127:
                    return 'spam'
                else:
                    if hasLinks:
                        return 'spam'
                    else:
                        return 'ham'
        else:
            if hasLinks:
                return 'spam'
            else:
                if lengthOfText > 159:
                    if lengthOfText > 161:
                        return 'ham'
                    else:
                        return 'spam'
                else:
                    return 'ham'
    else:
        if hasLinks:
            return 'spam'
        else:
            return 'ham'

def lambda_handler(event, context):
    sms = event['sms']
    
    try:
        prediction = makePrediction(sms)
        return {
            'statusCode': 200,
            'body': {
                'result': prediction
            }
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps("Error {}".format(e))
        }