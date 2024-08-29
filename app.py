#!/usr/bin/env python3
import views.certification
from flask import Flask
from convertor.date_converter import DateConverter
app = Flask(__name__)
app.url_map.converters['date'] = DateConverter


@app.route('/home')
@app.route('/information')
@app.route('/introduction')
def home():
    '''Home page'''
    return '''
    <html>
      <head><title>Online personal counseling system</title></head>
      <body>
         <h1>Online personal counseling system</h1>
          <p> Welcome to the online personal counseling system. This system is\
              design to help you with your personal issues. </p>
      </body>
   </html
   '''


app.add_url_rule(
    '/certificate/accomplishment/<string:name>/<string:course>/<date:\
      certification_date>', 'show_honor_dismissal',
    views.certification.show_honor_dismissal)


if __name__ == '__main__':
    app.run()
