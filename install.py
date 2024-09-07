import requests
import os

# 取得したいURL
url = "https://diamondgotcat.github.io/Tester-for-MathConsole/main.py"

# GETリクエストを送信し、レスポンスを取得
response = requests.get(url)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのテキストデータをファイルに書き込む
    os.mkdir("/usr/local/share/mathconsole/plugins/tester/main.py")
    with open("/usr/local/share/mathconsole/plugins/", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Installed")
else:
    print(f"Error Downloading: {response.status_code}")
