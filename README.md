language-translate
====

IBM Watsonを使って、日本語と英語の双方向翻訳をするアプリです。

## Description
Djangoで実装されています。

## Requirement
Python3.6  
certifi==2018.11.29  
chardet==3.0.4  
Django==2.1.5  
idna==2.8  
python-dateutil==2.7.5  
pytz==2018.9  
requests==2.21.0  
six==1.12.0  
urllib3==1.24.1  
watson-developer-cloud==2.5.4  
websocket-client==0.48.0  

## Usage
1. Githubからリポジトリをクローン
```
$ git clone https://github.com/Takumetal/language-translate.git
```
2. プロジェクトディレクトリに入る
```
$ cd language-translate
```
3. pipを使用して、必要なライブラリをインストール
```
$ pip install -r requirements.txt 
```
4. IBM WatsonのAPIキーを取得して、以下に設定する
```
translate/views.py
iam_apikey='',
```
5. Djangoの開発サーバーを起動
```
$ python manage.py runserver
```
6. ブラウザで以下のURLにアクセス
```
http://127.0.0.1:8000
```

## Licence
MIT

## Author
[Takumetal](https://github.com/Takumetal)
