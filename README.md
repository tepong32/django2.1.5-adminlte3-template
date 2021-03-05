# django2.1-adminlte3-template
A Django website template using AdminLTE3 &amp; Bootstrap theming

NOTES:
## This is my project in line with practicing the D-R-Y principle...or maybe not.

I'm trying to create a django website template which can be used over-and-over (with just minimal template mods necessary).
Backend-wise, I think this is a good starter template. Key features are as follows:


I specifically used AdminLTE3 so users can freely use FontAwesome icons without much changes on scripts included on 'home/index.html'.
Using plain Bootstrap, newbie devs will have to research as to how to add CSS links and scripts first for FontAwesome icons to work. Alternatively, you can use Material Icons made by Google. 

The site's 'settings.py' include MY OWN Google client and key for OAuth2 (django-allauth). Not like you will be able to use it in production but it's good for testing so, I left it there. Should you want to implement the same on your project websites, you'll have to create your own client-key-secret on https://console.developers.google.com. I strongly suggest that you use your researching skills and watch Django-Allauth tutorials on Youtube.

This sample template includes a "home" and a "user" app which, I think, are essential for any project website. If you plan to create a blog site, add a "blog" app and practice linking models, templates and urls yourself. That will definitely help you a lot. As in A LOT! ;)

Speaking of a "blog" app, I also added ckeditor to the "installed apps" list for Rich Text Editing. You'll just have to create your models and add the specific attributes you need.

Also, password-related stuffs were tested and are working as intended. You can modify the templates on "user/templates/password-reset". Just setup the fields needed by the system for sending emails to users' email addresses.

## Setting-up your production environment
I was able to setup a website on NameCheap.com using everything I included here. I just removed those "apps" that are specific to my site's needs.
If you need help setting-up a Django website on NameCheap's shared hosting, this article was what helped me: https://pythonfusion.com/deploy-django-on-shared-hosting/. My website's url: https://one.teppy.rocks.

## Running this on Django 3.0 showed no problems at all in the development environment but PyMySQL can only work on Django 2.1 on Namecheap's shared hosting

Just keep in mind that we (me and pythonfusion owner) specifically used Django 2.1 because we need support for PyMySQL database on NameCheap. We purchased the cheapest plan: Stellar (https://www.namecheap.com/hosting/shared/) so, we only have access to MySQL Databases. I'm not sure yet if using Django 3.0 can be set to support PyMySQL. If you purchase the Stellar Plus or Stellar Business plans tho, you'll have access to PostgreSQL databases and you can use the latest version of Django. Setting-up your PostgreSQL database, you will just need to watch tutorials. ;)

Also, I created a step-by-step process of purchasing and setting-up a website on NameCheap. You can check https://teppy.rocks/2021/02/11/setting-up-your-own-website/ and leave a comment to help me improve the article.

## Thank you.
 
