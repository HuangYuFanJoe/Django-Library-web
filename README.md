# Library-web
使用說明
- 需下載 Django框架 https://www.djangoproject.com/download/
- 在webtest資料夾(含有manage.py那個) 輸入sudo python3 manage.py runserver即可啟動服務
- 網址為127.0.0.1:8000/catalog
- 前端程式碼存在catalog/templates資料夾中

簡介<>
網站具登入、註冊、修改資料庫等功能
並依據會員的身分切割權限
- 普通圖書館會員只能查看自己借了哪些書
- 圖書館員工可看到所有已出借的書、並可幫會員續借書籍
- root比圖書館員工多了一個權限為可指定某人為圖書館員工
