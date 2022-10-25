import smtplib, ssl

def send(alpha, l): 
    s = l[0]
    f = l[1] 
    e = l[2]
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "dio.training.info@gmail.com"  # Enter your address
    receiver_email = "natusume@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = "Training for {} is done. \n success = {}, failures = {}, exhausts = {}".format(alpha, s, f, e)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

