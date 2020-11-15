from flask import Flask, url_for, request,render_template


webapp = Flask(__name__)

@webapp.route("/")
def index():
    return "Hello WOLRD"

@webapp.route("/ussd", methods = ['POST'])
def ussd():
  # Read the variables sent via POST from our API
  session_id   = request.values.get("sessionId", None)
  serviceCode  = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text         = request.values.get("text", "default")
  
  if text      == '':
      # This is the first request. Note how we start the response with CON
      response  = "CON What would you want to check \n"
      response += "1. My Account \n"
      response += "2. My phone number"

  elif text    == '1':
      # Business logic for first level response
      response  = "CON Choose account information you want to view \n"
      response += "1. Account number \n"
      response += "2. Account balance"

  elif text   == '2':
      # This is a terminal request. Note how we start the response with END
      response = "END Your phone number is " + phone_number

  elif text          == '1*1':
      # This is a second level response where the user selected 1 in the first instance
      accountNumber  = "ACC1001"
      # This is a terminal request. Note how we start the response with END
      response       = "END Your account number is " + accountNumber

  elif text    == '1*2':
      # This is a second level response where the user selected 1 in the first instance
      balance  = "KES 10,000"
      # This is a terminal request. Note how we start the response with END
      response = "END Your balance is " + balance

  else :
      response = "END Invalid choice"

  # Send the response back to the API
  return response

if __name__=="__main__":
    webapp.run(debug=True)