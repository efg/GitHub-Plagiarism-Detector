import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
        
# This will email the instructor after each run listing the maximum jumps (percentage increase in similarities in the current run when compared to previous run).
def email_jump_info(jumps: list=None, check_id: int=None)->None:
    #reading the required variables to send email from .env file
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    password = os.getenv('APP_PASSWORD')

    #initialising to, from and subject for the email
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Github Plagiarism Detector - Check " + str(check_id)
    text = ""
    #Email format when there is a previous run to compare
    # creating  table header and brief info about each columns 
    if jumps:
        html = """\
                <html>
                    <head>
                        <style> 
                            table, th, td {
                                border: 1px solid white;
                                border-collapse: collapse;
                            }
                            th, td {
                                background-color: #96D4D4;
                            }
                            .alnright { text-align: right; }
                        </style>
                    </head>
                    <body>
                        <div>
                            <div>
                                <p><b>Below table indicates the top jumps for this check </b> </p>
                                <p><b>NOTE:</b></p>
                                <p><b>Repo A and Repo B :</b> These two columns indicate the team names whose code is being checked.</p>
                                <p><b>Shared Code Repo A to B :</b> This column indicates percentage of first team A’s code that is shared with second team B for the current run.</p>
                                <p><b>Similarity Jump Repo A to B:</b> This column indicates the difference between the similarity percentage of Team A with Team B from current run to previous run.</p>
                                <p><b>Shared Code Repo B to A :</b> This column indicates percentage of first team B’s code that is shared with second team A for the current run.</p>
                                <p><b>Similarity Jump Repo B to A:</b> This column indicates the difference between the similarity percentage of Team B with Team A from current run to previous run.</p>
                            </div>
                            <div>
                                <table>
                                    <tr>
                                        <th>Repo A</th>
                                        <th>Repo B</th>
                                        <th>Shared Code Repo A to B</th>
                                        <th>Shared Code Repo A to B</th>
                                        <th>Similarity Jump Repo A to B</th>
                                        <th>Similarity Jump Repo B to A</th>
                                    </tr>
                """
        #creating table rows which will have jump info.
        for x in jumps:
            html += "<tr><td class='alnright'>" + str(x[0]) + "</td><td class='alnright'>" + str(x[1])+ "</td><td class='alnright'>" + str(x[2])+"%" + "</td><td class='alnright'>" + str(x[3])+ "%"  + "</td><td class='alnright'>" + str(x[4]) +"%"+ "</td><td class='alnright'>" + str(x[5]) +"%" + "</td></tr>"

        html += """\
                                </table>
                            </div>
                        </div>
                    </body> 
                </html>
            """
    #Email format when there is no previous run 
    else:
        html = """\
            <html>
                <body>
                    <div>
                        <p> This is the first run. Hence can not report a change in similarity. </p>
                    </div>
                </body>
            </html>
            """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
