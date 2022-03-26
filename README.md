# django-example-project

## 環境構築手順

### 1.コードをローカル(dockerインストール済)にクローン、.envを共有(GitHub上には無い)


### 2.プロジェクト直下で下記コマンド実行
2-1.
`docker-compose build`

2-2.
`docker-compose run web python manage.py makemigrations myapp`

2-3.
`docker-compose run web python manage.py migrate --run-syncdb`

2-4.
`docker-compose run web python manage.py migrate myapp`

2-5.
`docker-compose run web python manage.py createsuperuser`  
(※登録データ確認のため、任意のユーザー名/Eメール/パスワードでスーパーユーザー登録)

2-6.ローカルホストで立ち上げ  
`docker-compose up -d`

2-7.
下記にアクセスし、作成したスーパーユーザーでログインできるのを確認  
http://localhost:8000/admin/

### ※2.開発時にDockerを使わず起動する場合
2-1.
`python manage.py makemigrations myapp`

2-2.
`python manage.py migrate --run-syncdb`

2-3.
`python manage.py migrate myapp`

2-4.
`python manage.py createsuperuser`
(※登録データ確認のため、任意のユーザー名/Eメール/パスワードでスーパーユーザー登録)

2-5.ローカルホストで立ち上げ 
`python manage.py runserver 0.0.0.0:8000`

2-6.
下記にアクセスし、作成したスーパーユーザーでログインできるのを確認  
http://localhost:8000/admin/


### 3.APIをHTTPリクエストで確認
3-1.アルコール飲料を登録するAPI 
関数のパス：myapp/view.py/saveProducts(name, product_type, manufacturer, degree, price)  
・リクエスト例
```
POST http://localhost:8000/myapp/save_products/
Accept: */*
Cache-Control: no-cache
X-Requested-With: XMLHttpRequest
Content-Type: application/json

{
  "name": "Asahi super dry",
  "product_type": "beer",
  "manufacturer": "ASAHI BREWERIES",
  "degree": "5.0",
  "price": "460"
}

POST http://localhost:8000/myapp/save_products/
Accept: */*
Cache-Control: no-cache
X-Requested-With: XMLHttpRequest
Content-Type: application/json

{
  "name": "Spring Valley",
  "product_type": "beer",
  "manufacturer": "Kirin Holdings",
  "degree": "6.0",
  "price": "248"
}

```
※name/type/manufacturerの文字数は30文字まで。degreeは小数点第一位までで0-100、priceは整数のみで0-10000。  

※入力済データは、下記で確認可能  
http://localhost:8000/admin/myapp/alcoholicproduct/

※既に存在するname/type/manufacturerの組み合わせが入力された場合は、既存のレコードを更新

3-2.同じ種類(type)のアルコール飲料の中で最大の度数のものを返す(最も高い度数のものが複数あった場合はその内の1つ)  
関数のパス：myapp/view.py/getHighestDegreeProducts(type)  
・リクエスト例
```
GET http://localhost:8000/myapp/get_high_alcohol_product/?product_type=beer
Accept: */*
Cache-Control: no-cache
X-Requested-With: XMLHttpRequest
Content-Type: application/json

```

### 4.終了
docker-compose down
