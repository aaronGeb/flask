from datetime import date
from app import app


@app.route('/certificate/accomplishment/<string:name>/<string:course>/<date:\
           certification_date>')
def certificate_accomplishment(name: str, course: str, certification_date:
                               date):
    '''Certificate of accomplishment'''
    return f'''
    <html>
      <head><title>Certificate of accomplishment</title></head>
      <body>
         <h1>Certificate of accomplishment</h1>
          <p> This is to certify that {name} has successfully completed the\
              course {course} on {certification_date}. </p>
      </body>
   </html
   ''', 200


def show_honor_dismissal(counselor: str, effective_date: date, patient: str,
                         reason: str):
    '''letter of termination of consultation'''
    return f'''
    <html>
      <head><title>Termination of Consultation</title></head>
      <body>
         <h1>Termination of Consultation</h1>
         <p> From: {counselor} </p>
         <p> Head of the Counseling Department </p>
         <p> Date: {effective_date} </p>
         <p> To: {patient} </p>
         <p>SUBJECT: Termination of Consultation</p>
          <p> Dear {patient}, </p>
          <p> I am writing to inform you that your consultation has been \
            terminated due to {reason}. </p>
          <p> If you have any questions, please do not hesitate to contact me. </p>
          <p> Sincerely, </p>
          <p> {counselor} </p>
      </body>
   </html
   ''', 200
