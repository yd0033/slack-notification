from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack APIトークンとチャンネル設定
TOKEN = "YOUR_SLACK_API_TOKEN_HERE"  # Slack APIトークンを設定
CHANNEL = "YOUR_SLACK_CHANNEL_ID_HERE"  # SlackチャンネルIDを設定

# 生成されるテキストファイルの情報
FILENAME = "generated_file.txt"
FILEPATH = r"./"
TEXT_CONTENT = (
    "This is a sample text content for the uploaded file."  # 生成されるファイル内に書き込むテキスト
)


# テキストファイルを生成する関数（送信するファイルがある場合は不要）
def create_text_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)


# ファイルをSlackにアップロードする関数
def upload_file_with_params(params):
    try:
        client = WebClient(token=params["token"])
        response = client.files_upload_v2(
            channel=params["channel"],
            file=params["filepath"],
            filename=params["filename"],
            initial_comment=params["initial_comment"],
            title=params["title"],
        )
        print("File uploaded successfully!")
        print("Response:", response)
    except SlackApiError as e:
        print(f"Error uploading file: {e.response['error']}")


if __name__ == "__main__":
    create_text_file(FILEPATH + FILENAME, TEXT_CONTENT)

    params_list = [
        {
            "token": TOKEN,
            "channel": CHANNEL,
            "filename": FILENAME,
            "filepath": FILEPATH + FILENAME,
            "initial_comment": "Here is the first file!",
            "title": "File Upload Example 1",
        },
        {
            "token": TOKEN,
            "channel": CHANNEL,
            "filename": FILENAME,
            "filepath": FILEPATH + FILENAME,
            "initial_comment": "Here is the second file!",
            "title": "File Upload Example 2",
        }
        # 他のパラメータセットも追加可能
    ]
    for params in params_list:
        upload_file_with_params(params)
