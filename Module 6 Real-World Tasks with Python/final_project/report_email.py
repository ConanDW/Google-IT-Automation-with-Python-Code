#!/usr/bin/env python3
import os
import datetime
import reports
import emails

def get_fruit_data(path):
    names = []
    weights = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            with open(file_path) as f:
                for ln in f:
                    line = ln.strip()
                    if len(line) <= 10 and len(line) > 0 and "lb" not in line:
                        fruit_name = f"name: {line}"
                        names.append(fruit_name)
                    if "lbs" in line:
                        fruit_weight = f"weight: {line}"
                        weights.append(fruit_weight)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
    return names, weights

def create_summary(names, weights):
    summary = ""
    for name, weight in zip(names, weights):
        summary += f"{name}<br />{weight}<br /><br />"
    return summary

if __name__ == "__main__":
    dt = datetime.date.today().strftime("%B %d, %Y")
    date = f"Processed Update on {dt}"
    path = "./supplier-data/descriptions/"
    
    names, weights = get_fruit_data(path)
    summary = create_summary(names, weights)
    
    reports.generate_report("/tmp/processed.pdf", date, summary)
    
    sender = "automation@example.com"
    receiver = f"{os.environ.get('USER')}@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
