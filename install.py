import requests

# 取得したいURL
url = "https://diamondgotcat.github.io/Tester-for-MathConsole/main.py"

# GETリクエストを送信し、レスポンスを取得
response = requests.get(url)

# レスポンスのステータスコードを確認
if response.status_code == 200:
    # レスポンスのテキストデータをファイルに書き込む
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Installed")
else:
    print(f"Error Downloading: {response.status_code}")
