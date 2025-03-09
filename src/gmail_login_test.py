import smtplib, os
from dotenv import load_dotenv

smtp_server = "smtp.gmail.com"
smtp_port = 465

load_result = load_dotenv()
if not load_result:
    raise Exception(".env 檔案載入失敗")

email = os.getenv("SENDER_EMAIL")
password = os.getenv("SENDER_PASSWORD")
print(f"email={email}, password={password}")

try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(email, password)
    print("✅ SMTP 登入成功！")
except Exception as e:
    print(f"SMTP 登入失敗: {e}")
finally:
    server.quit()