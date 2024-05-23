def write_notification(email: str, mensagem=""):
    with open("log.txt", mode="a") as email_file:
        content = f"Email: {email} - msg: {mensagem}\n"
        email_file.write(content)
