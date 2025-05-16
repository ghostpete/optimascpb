def send_transaction_mail(to_email, message, subject="OTP Verification"):
    # Email content
    subject = subject
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1738846522/2_j6hl89.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>Your transaction is almost complete.</p>
            <p>{message}</p>
            
            <p>If you didn't request perform a transaction, please ignore this email.</p>
            <p>Thanks for banking with us.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 Cyprus Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"Cyprus Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    
    
    try:
        with smtplib.SMTP(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.starttls()
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        print("Password reset email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")






def send_transaction_mail(to_email, message, subject="OTP Verification"):
    # Email content
    subject = subject
    html_content = f"""
    <html>
    <body>
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; padding: 20px;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="https://res.cloudinary.com/daf9tr3lf/image/upload/v1738846522/2_j6hl89.png" alt="Logo" style="width: 150px;"/>
            </div>
            <p>Your transaction is almost complete.</p>
            <p>{message}</p>
            
            <p>If you didn't request perform a transaction, please ignore this email.</p>
            <p>Thanks for banking with us.</p>
            <p style="text-align: center; font-size: 14px; color: #777; margin-top: 30px;">
                © 2025 Cyprus Bank. All rights reserved.
            </p>
        </div>
    </body>
    </html>
    """
    
    msg = MIMEMultipart()
    msg['From'] = f"Cyprus Bank <{FROM_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))
    

    try:
        # Set up the SMTP server connection using SSL
        with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as server:
            server.login(ADMIN_EMAIL, EMAIL_PASSWORD)  # Log in with Hostinger credentials
            
            # Send the email
            server.sendmail(ADMIN_EMAIL, to_email, msg.as_string())
        
        print(f"HTML email successfully sent to {ADMIN_EMAIL}!")
    except Exception as e:
        print(f"Failed to send email to {ADMIN_EMAIL}: {e}")

