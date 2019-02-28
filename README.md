language-translate
====

IBM Watsonを使って、日本語と英語の双方向翻訳をするアプリです。  
This is an app that uses IBM Watson to translate both Japanese and English.

## Description
Djangoで実装されています。  
It is implemented in Django.

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
Clone repository from Github
```
$ git clone https://github.com/Takumetal/language-translate.git
```
2. プロジェクトディレクトリに入る  
Change the project directory
```
$ cd language-translate
```
3. pipを使用して、必要なライブラリをインストール  
Install required libraries using pip
```
$ pip install -r requirements.txt 
```
4. IBM WatsonのAPIキーを取得して、以下に設定する  
Get the API key for the Azure Bing Image Search API and set it as follows.
```
translate/views.py
iam_apikey='',
```
5. Djangoの開発サーバーを起動  
Launch the development server for Django
```
$ python manage.py runserver
```
6. ブラウザで以下のURLにアクセス  
Access the following URL in a browser
```
http://127.0.0.1:8000
```

## Licence
MIT

## Author
[Takumetal](https://github.com/Takumetal)
