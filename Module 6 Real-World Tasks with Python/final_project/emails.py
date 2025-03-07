#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib
import logging

logging.basicConfig(level=logging.DEBUG)

def generate_email(sender, recipient, subject, body, attachment_path=None):
    """Creates an email with or without an attachment."""
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    if attachment_path:
        try:
            attachment_filename = os.path.basename(attachment_path)
            mime_type, _ = mimetypes.guess_type(attachment_path)
            mime_type, mime_subtype = mime_type.split('/', 1)

            with open(attachment_path, 'rb') as ap:
                message.add_attachment(ap.read(),
                                    maintype=mime_type,
                                    subtype=mime_subtype,
                                    filename=attachment_filename)
            logging.debug(f"Attachment {attachment_filename} added to the email.")
        except Exception as e:
            logging.error(f"Failed to add attachment: {e}")

    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    try:
        mail_server = smtplib.SMTP('localhost')
        mail_server.send_message(message)
        mail_server.quit()
        logging.debug("Email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")


if __name__ == "__main__":
    import report_email

    sender = "automation@example.com"
    receiver = f"{os.environ.get('USER')}@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"

    message = generate_email(sender, receiver, subject, body, attachment_path)
    send_email(message)
