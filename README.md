# CHAT
creating simple chat app
## Requirements
App run od redis, before launch

**$ docker run -p 6379:6379 -d redis:5**

rest in requirements.txt

**API ENDPOINTS:**
1. [ Chat. ](#rest)
2. [ Rest. ](#chat)

<a name="rest"></a>
## 1. Rest


You need to see documentation again. You can see this cheatsheet

In your case you need to make second line like in example below:

Url | View | Name 
--- | --- | --- 
/api-auth/login/ | django.contrib.auth.views.LoginView | rest_framework:login 
/api-auth/logout/ | django.contrib.auth.views.LogoutView |rest_framework:logout
 /login/ | django.contrib.auth.views.LoginView | login
 /logout/ | django.contrib.auth.views.LogoutView | logout
 /password_change/ | django.contrib.auth.views.PasswordChangeView | password_change 
 /password_change/done/ | django.contrib.auth.views.PasswordChangeDoneView | password_change_done 
 /password_reset/ | django.contrib.auth.views.PasswordResetView | password_reset 
 /password_reset/done/ | django.contrib.auth.views.PasswordResetDoneView | password_reset_done 
 /posts/ | login.api.CreatePostsView | post-list  
 /posts/<pk>/ | login.api.CreatePostsView | post-detail 
 /profile/ | login.api.CreateProfileView | profile-list 
 /reset/<uidb64>/<token>/ | django.contrib.auth.views.PasswordResetConfirmView | password_reset_confirm 
 /reset/done/ | django.contrib.auth.views.PasswordResetCompleteView | password_reset_complete 
 /users/ | login.api.CreateUserView | user-list 


<a name="chat"></a>
## 2. Chat

Room name is a cutom url check chat/routing.py for details

Url | Info
-- | --
ws/chat/<str:room_name> | custom room_name
