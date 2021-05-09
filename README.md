# Завданння:
## Хапай-файлопередай
Розробити сервіс поширення фалів на кшталт MEGA, RGhost автор файлу отримує унікальне посилання прямого доступу, яке він може передати іншому користувачу автор може переглянути всі свої розміщені файли автор може задати “час життя” файлу після закінчення “часу життя” файл перестає бути доступний всім, але залишається в системі Інтерфейс користувача повинен містити перелік доступних файлів випадкове відображення файлу випадкове відображення файлу, який перестане бути доступним менше ніж за певний час(годину, добу, тиждень) статистику: скільки всього було завантажено файлів, скільки доступно зараз, скільки перестане бути доступними через певний час (добу, годину) Інтеграція з соціальними мережами: Додати вхід через популярні соціальні мережі:
Facebook (https://developers.facebook.com/docs/facebook-login)
Google (https://developers.google.com/identity/)
Інші соцмережі на ваш вибір (необов'язково)

##Whoa, It Worked

Запуск: для коректної роботи аутентифікації через google та facebook(тут провина facebook api) треба запускати з неявним localhost, тобто: 
Windows: `python manage.py runserver localhost:8000`
Mac\Linux: `python3 manage.py runserver localhost:8000`

>(Перед розгортанням на хостингу - пройтись по адмін панелям соц.мереж і додати IP-адресу в whitelist-и)

Додано файл `requirements.txt` - для інсталяції всього добра: 
Windows: `py -m pip install -r requirements.txt`
Mac\Linux: `python3 -m pip3 install -r requirements.txt`

##Screenshots:

+ HomeScreen
![HomeScreen](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/HomeScreen.png?raw=true)
+ SignUp
![SignUp](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/SignUp.png?raw=true)
+ Login
![Login](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Login.png?raw=true)

+ Alerts:
![Alert1](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Alert1.png?raw=true)
![Alert2](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Alert2.png?raw=true)
![Alert3](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Alert3.png?raw=true)
![Alert4](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Alert4.png?raw=true)

+ AboutUser
![AboutUser](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/AboutUser.png?raw=true)
+ NewFileForm
![NewFileForm](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/NewFileForm.png?raw=true)
+ Upload
![Upload](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Upload.png?raw=true)
+ UploadSuccess
![UploadSuccess](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/UploadSuccess.png?raw=true)
+ Navigation:
![Navigation1](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Navigation1.png?raw=true)
![Navigation2](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Navigation2.png?raw=true)
+ Search
![Search](https://github.com/Vionikk/djangoFileHostingAppDesign/blob/main/README/Search.png?raw=true)


# Practic
 Ці команди вводяться в git bash або в консолі якщо ви при установці вказали роботу з гітом через консоль; 
 
 перед введенням команд потрібно перейти в директорію вашого проекту (якщо через баш то можна перейти в папку там пкм і вибрати git bash)

#  Для нового проекта робіть нову гілку
`git init` - якщо просто оновлення то без цього

`git add *`

`git commit -m "коміт шоб було понятно шо за хуйню ви кидаєте"`

`git remote add origin https://github.com/Goosefrom/practic`

`git push origin <назва гілки в яку хочете закинути>`

# Клонувати проект собі на компухтєр
`git clone <адреса яка появляється після нажатія на зелену кнопочку code>`
(тільки слідкуйте за гілкою бо я так пару раз проїбався колись)

`git pull` - оновити репозиторій в себе на машині

# Робота з гілками
+ перехід  на основну гілку: `git checkout front`
+ створити нову гілку і одразу перейти на неї: `git checkout -b <newBranchName>`
+ вивести всі гілки репозиторію: `git branch -a`



While using a free bootstrap template:
![HomeScreen](https://www.meme-arsenal.com/memes/118e17b1cef68b5af7a9eb5829de068a.jpg?raw=true)
