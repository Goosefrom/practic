# Завданння:
## Хапай-файлопередай
Розробити сервіс поширення фалів на кшталт MEGA, RGhost автор файлу отримує унікальне посилання прямого доступу, яке він може передати іншому користувачу автор може переглянути всі свої розміщені файли автор може задати “час життя” файлу після закінчення “часу життя” файл перестає бути доступний всім, але залишається в системі Інтерфейс користувача повинен містити перелік доступних файлів випадкове відображення файлу випадкове відображення файлу, який перестане бути доступним менше ніж за певний час(годину, добу, тиждень) статистику: скільки всього було завантажено файлів, скільки доступно зараз, скільки перестане бути доступними через певний час (добу, годину) Інтеграція з соціальними мережами: Додати вхід через популярні соціальні мережі:
Facebook (https://developers.facebook.com/docs/facebook-login)
Google (https://developers.google.com/identity/)
Інші соцмережі на ваш вибір (необов'язково)
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
