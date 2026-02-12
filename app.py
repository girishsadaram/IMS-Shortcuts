from flask import Flask, render_template

app = Flask(__name__)

# Add your shortcut URLs here
shortcuts = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "ChatGPT", "url": "https://chat.openai.com"},
    {"name": "Pena4 Homepage", "url": "https://auditoolstorage.blob.core.windows.net/fileupload/pena4sites.html"},
    {"name": "System Utilization", "url": "http://10.100.10.27:8080/"},
    {"name": "GitLab", "url": "http://10.100.10.238/"},
    {"name": "Dev Portal", "url": "https://dev.azure.com/Pena4Inc/"},
    {"name": "Exit Checklist", "url": "https://softwarechangerequestform.azurewebsites.net/exitForm"},
    {"name": "Asset Aggrement", "url": "https://auditoolstorage.blob.core.windows.net/fileupload/HR_Asset_Aggrement.html"},
    {"name": "Welcome Letter", "url": "https://softwarechangerequestform.azurewebsites.net/welcomLetter"},
    {"name": "Cloud Antivirus", "url": "https://access.broadcom.com/"},
    {"name": "O365 Admin Center", "url": "https://admin.cloud.microsoft/?source=applauncher#/homepage"},
    {"name": "FreshDesk", "url": "https://pena4.freshdesk.com/support/login"},
 ]

@app.route("/")
def home():
    return render_template("index.html", shortcuts=shortcuts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
