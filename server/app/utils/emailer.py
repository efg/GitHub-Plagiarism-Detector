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
    max_jump = int(os.getenv('MAXIMUM_JUMP_PERCENTAGE'))

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
                                border: 1px solid black;
                                border-collapse: collapse;
                                padding-top: 5px;
                                padding-bottom: 5px;
                                padding-left: 5px;
                                padding-right: 5px;
                            }
                            .alnright { text-align: right; }
                        </style>
                    </head>
                    <body>
                        <div>
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
            if x[4] > max_jump and x[5] > max_jump:
                html += "<tr><td class='alnright'>" + str(x[0]) + "</td><td class='alnright'>" + str(x[1])+ "</td><td class='alnright'>" + str(x[2])+"%" + "</td><td class='alnright'>" + str(x[3])+ "%"  + "</td><td class='alnright' style='color:#ea0b22'>" + str(x[4]) +"%"+ "</td><td class='alnright' style='color:#ea0b22'>" + str(x[5]) +"%" + "</td></tr>"
            elif x[4] > max_jump:
                html += "<tr><td class='alnright'>" + str(x[0]) + "</td><td class='alnright'>" + str(x[1])+ "</td><td class='alnright'>" + str(x[2])+"%" + "</td><td class='alnright'>" + str(x[3])+ "%"  + "</td><td class='alnright' style='color:#ea0b22'>" + str(x[4]) +"%"+ "</td><td class='alnright'>" + str(x[5]) +"%" + "</td></tr>"
            elif x[5] > max_jump:
                html += "<tr><td class='alnright'>" + str(x[0]) + "</td><td class='alnright'>" + str(x[1])+ "</td><td class='alnright'>" + str(x[2])+"%" + "</td><td class='alnright'>" + str(x[3])+ "%"  + "</td><td class='alnright'>" + str(x[4]) +"%"+ "</td><td class='alnright' style='color:#ea0b22'>" + str(x[5]) +"%" + "</td></tr>"
            else:
                html += "<tr><td class='alnright'>" + str(x[0]) + "</td><td class='alnright'>" + str(x[1])+ "</td><td class='alnright'>" + str(x[2])+"%" + "</td><td class='alnright'>" + str(x[3])+ "%"  + "</td><td class='alnright'>" + str(x[4]) +"%"+ "</td><td class='alnright'>" + str(x[5]) +"%" + "</td></tr>"

        html += """\
                                </table>
                            </div>
                            <div>
                                <p><b>NOTE:</b></p>
                                <table>
                                    <tr>
                                    <th>Column Name</th>
                                    <th>Description</th>
                                    </tr>
                                    <tr>
                                    <td>Repo A</td>
                                    <td>Code of Team A being checked</td>
                                    </tr>
                                    <tr>
                                        <td>Repo B</td>
                                        <td>Code of Team B being checked</td>
                                    </tr>
                                    <tr>
                                        <td>Shared Code Repo A to B</td>
                                        <td>Percentage of first team A&apos;s code that is shared with second team B for the current run</td>
                                    </tr>
                                    <tr>
                                        <td>Similarity Jump Repo A to B</td>
                                        <td>Difference between the similarity percentage of Team A with Team B from current run to previous run</td>
                                    </tr>
                                    <tr>
                                        <td>Shared Code Repo B to A</td>
                                        <td>Percentage of first team B&apos;s code that is shared with second team A for the current run</td>
                                    </tr>
                                    <tr>
                                        <td>Similarity Jump Repo B to A</td>
                                        <td>Difference between the similarity percentage of Team B with Team A from current run to previous run</td>
                                    </tr>
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
