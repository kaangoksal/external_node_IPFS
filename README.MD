This is a template for Kaan's Flask Apps, I just like the way that this is structured.

You start the app with 


uwsgi --socket 0.0.0.0:80 --protocol=http -w wsgi  

where wsgi is the py file that has the application imported
