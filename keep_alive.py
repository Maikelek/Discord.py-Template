# from flask import Flask
# from threading import Thread

# app = Flask("")
# @app.route("/")
# def home():
#   return "Bot is logged"

# def run():
#   app.run(host="0.0.0.0", port=8080)

# def keep_alive():
#   t = Thread(target=run)
#   t.start()


  #If you are hosting via net services ... for example replit
  #Uncomment 1-14 line here and in main.py uncomment 7th line (#from keep_alive import keep_alive) 
  #Flask will make "web server"
  #Find any service that can check if your server is online (any free pinging service that keeps pinging)
  #Bot will be online 24/7 except for some problems of pinging service that keeps you alive
