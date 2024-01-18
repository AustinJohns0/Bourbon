from django.shortcuts import render
from django.template import context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.http import HttpResponse

def sendmail(request):
    ctx={
        'name':'aroma',
        'message':'Hello,this is a text mail',
    }
    message =get_template('index.html').render(ctx)
    try:
       msg =EmailMessage(
           'subject',
           message,
           'austinkjohns@gmail.com',
           ['aroma95chand@gmail.com'],

       )
       msg.content_subtype='html'
       msg.send()
       print("mail sent")
       return HttpResponse('mail sent')
    except Exception as e:
       print('Error sending mail',str(e))
       return HttpResponse("Error sending mail:"+str(e))

