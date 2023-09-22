import tkinter as tk
import smtplib
from tkinter import messagebox
from tkinter import filedialog

# Create lists to store sent and draft emails
sent_emails = []
draft_emails = []

# Function to send the email
def send_email():
    try:
        # Get user input from the GUI
        recipient = recipient_entry.get()
        subject = subject_entry.get()
        message = message_text.get("1.0", tk.END)  # Corrected the get() method

        # Connect to Gmail's SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_username = "subham8571@gmail.com"
        smtp_password = "wodb rdvk zwao gwoh"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Compose and send the email
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(smtp_username, recipient, email_message)
        server.quit()

        # Save the sent email
        save_sent_email(recipient, subject, message)

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("Simple Mail Application")
window.geometry("1920x1080")  # Set the initial window size

# Create and arrange widgets
recipient_label = tk.Label(window, text="Recipient:")
recipient_label.pack()
recipient_entry = tk.Entry(window, width=50)  # Increase width
recipient_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window, width=50)  # Increase width
subject_entry.pack()

message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=10, width=50)  # Increase height and width
message_text.pack()

send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()

# Function to attach a file
def attach_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        # Display the attached file's name in the GUI or perform further actions
        attachment_label.config(text=f"Attached: {file_path}")

# Create an "Attach File" button
attach_button = tk.Button(window, text="Attach File", command=attach_file)
attach_button.pack()

# Create a label to display attached file information
attachment_label = tk.Label(window, text="")
attachment_label.pack()

# Function to reply to an email
def reply_email():
    original_recipient = recipient_entry.get()
    original_subject = subject_entry.get()
    original_message = message_text.get("1.0", tk.END)  # Corrected the get() method

    # Pre-fill recipient and subject fields
    recipient_entry.delete(0, tk.END)
    recipient_entry.insert(0, original_recipient)
    subject_entry.delete(0, tk.END)
    subject_entry.insert(0, f"Re: {original_subject}")

    # Pre-fill message with quoted original message
    quoted_message = f"\n\nOn {tk.datetime.datetime.now()} {original_recipient} wrote:\n{original_message}"
    message_text.delete("1.0", tk.END)
    message_text.insert(tk.END, quoted_message)

# Create a "Reply" button
reply_button = tk.Button(window, text="Reply", command=reply_email)
reply_button.pack()

# Function to forward an email
def forward_email():
    forward_window = tk.Toplevel(window)
    forward_window.title("Forward Email")

    # Create and arrange widgets in the forward window
    recipient_label = tk.Label(forward_window, text="Recipient:")
    recipient_label.pack()
    recipient_entry = tk.Entry(forward_window, width=50)  # Increase width
    recipient_entry.pack()

    subject_label = tk.Label(forward_window, text="Subject:")
    subject_label.pack()
    subject_entry = tk.Entry(forward_window, width=50)  # Increase width
    subject_entry.pack()

    message_label = tk.Label(forward_window, text="Message:")
    message_label.pack()
    message_text = tk.Text(forward_window, height=10, width=50)  # Increase height and width
    message_text.pack()

# Function to save a draft email
def save_draft():
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)  # Corrected the get() method
    
    draft = {
        'recipient': recipient,
        'subject': subject,
        'message': message
    }
    
    draft_emails.append(draft)
    messagebox.showinfo("Success", "Draft saved successfully!")

# Function to display the list of draft emails
def show_drafts():
    draft_window = tk.Toplevel(window)
    draft_window.title("Drafts")
    
    for draft in draft_emails:
        tk.Label(draft_window, text=f"Subject: {draft['subject']}").pack()
        tk.Label(draft_window, text=f"Recipient: {draft['recipient']}").pack()
        tk.Label(draft_window, text=f"Message: {draft['message']}").pack()

# Create a "Save Draft" button
save_draft_button = tk.Button(window, text="Save Draft", command=save_draft)
save_draft_button.pack()

# Create a "Show Drafts" button
show_drafts_button = tk.Button(window, text="Show Drafts", command=show_drafts)
show_drafts_button.pack()

# Function to save sent email
def save_sent_email(recipient, subject, message):
    sent = {
        'recipient': recipient,
        'subject': subject,
        'message': message
    }
    
    sent_emails.append(sent)

# Function to display the list of sent emails
def show_sent_items():
    sent_window = tk.Toplevel(window)
    sent_window.title("Sent Items")
    
    for sent in sent_emails:
        tk.Label(sent_window, text=f"Subject: {sent['subject']}").pack()
        tk.Label(sent_window, text=f"Recipient: {sent['recipient']}").pack()
        tk.Label(sent_window, text=f"Message: {sent['message']}").pack()

# Create a "Show Sent Items" button
show_sent_items_button = tk.Button(window, text="Show Sent Items", command=show_sent_items)
show_sent_items_button.pack()

# Create a "Forward" button
forward_button = tk.Button(window, text="Forward", command=forward_email)
forward_button.pack()

# Start the GUI main loop
window.mainloop()
