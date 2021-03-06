from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import logic
import ast

app = Flask(__name__)
cors = CORS()
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def welcome():
    try:
        byte_str = request.get_data()
        dict_str = byte_str.decode("UTF-8")
        data = ast.literal_eval(dict_str)

        return logic.addDynamic(data["schedule"], data["dynamic_slots"])
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='localhost', port=8000)

'''
curl -X GET 172.26.9.106:8000 -d '{"schedule": {"Monday":{"08:00":"SO","09:00":"Free","16:00":"PA","17:15":"LC","19:45":"Free"},"Tuesday":{"08:00":"Free", "13:30":"PA", "14:00": "Free"},"Wednesday":{"09:00":"PI","11:00":"LA1","15:00":"AUC","17:00":"Free"},"Thursday":{"14:00":"Violino","18:00":"Free"},"Friday":{"11:00":"PI","17:00":"LC","19:00":"Free"}},"dynamic_slots" : {"Ginasio":{"hours":"01:00","morning":False,"afternoon":True,"night":False,"late_night":False,"days":{"Monday":False,"Tuesday":True,"Wednesday":True,"Thursday":False,"Friday":True},"time":"01:00","is_fixed":True},"Passearocao":{"hours":"02:00","morning":False,"afternoon":False,"night":True,"late_night":False,"days":{"Monday":False,"Tuesday":False,"Wednesday":True,"Thursday":False,"Friday":True},"time":"00:30","is_fixed":False}}}' -H "Content-Type: application/json"

{"schedule": {"Monday":{"08:00":"SO","09:00":"Free","16:00":"PA","17:15":"LC","19:45":"Free"},"Tuesday":{"08:00":"Free", "13:30":"PA", "14:00": "Free"},"Wednesday":{"09:00":"PI","11:00":"LA1","15:00":"AUC","17:00":"Free"},"Thursday":{"14:00":"Violino","18:00":"Free"},"Friday":{"11:00":"PI","17:00":"LC","19:00":"Free"}},"dynamic_slots" : {"Ginasio":{"hours":"01:00","morning":False,"afternoon":True,"night":False,"late_night":False,"days":{"Monday":False,"Tuesday":True,"Wednesday":True,"Thursday":False,"Friday":True},"time":"01:00","is_fixed":True},"Passearocao":{"hours":"02:00","morning":False,"afternoon":False,"night":True,"late_night":False,"days":{"Monday":False,"Tuesday":False,"Wednesday":True,"Thursday":False,"Friday":True},"time":"00:30","is_fixed":False}}}

'''
