from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.shortcuts import redirect
from .models import *
from django.template.defaultfilters import date as _date
from datetime import datetime
import json
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from kids.models import TestimonialsKids

from news.models import *
import requests

from .template_mail import TmpMail
import json
import urllib
from collections import OrderedDict




def Price_ekb(request):
    price = PriceEkb.objects.all()
    category = []
    sub_category = []
    for a in price:
        category.append(a.category.name)
        sub_category.append(a.sub_category.name)

    category = list(OrderedDict.fromkeys(category))
    sub_category = list(OrderedDict.fromkeys(sub_category))

    #print(sub_category)

    mass = []

    for a in category:
        mass.append({'category':a,'data':[]})
        for b in sub_category:
            mass[category.index(a)]['data'].append({'sub_category':b,'data':[]})
            for c in price:
                if c.category.name == a and c.sub_category.name == b:
                    mass[category.index(a)]['data'][sub_category.index(b)]['data'].append({'name':c.name,'price':c.price,'link_pyment':c.link_pyment,'payment':c.payment})




    print(mass)
    #return render(request,'price.html',{'price':price,'category':category})
    return render(request,'price.html',{'mass':mass,'price':price})



def DocktorsItem(request,sid):
    doc = Doctors.objects.get(id=sid)
    return render(request,'doc-item.html',{'doc':doc,'title_seo':doc.name,'keywords_seo':doc.work_extention,'description_seo':doc.work_extention})


def GetDocMale(request):
    mass=[]
    doc = Doctors.objects.filter(work='врач уролог')
    for a in doc:
        mass.append({'id':a.id,'name':a.name,'image':str(a.image1),'work':a.work})

    return HttpResponse(json.dumps(mass))



def LogoOg(request):
    return render(request,'logo.html')



def GetDocFemale(request):
    #[3,8,7,9,10,11,13,14,15,16,37,36,42,45,46,47,49,50,52,53]
    mass=[]
    doc = Doctors.objects.filter(pk__in=[3,8,7,9,10,11,13,14,15,16,37,36,42,45,46,47,49,50,52,53]).order_by('?')[:4]
    for a in doc:
        mass.append({'id':a.id,'name':a.name,'image':str(a.image1),'work':a.work})

    return HttpResponse(json.dumps(mass))



def GetTestimonialsOnline(request):
    mass=[]
    doc = Testimonials.objects.filter(pk__in=[475,509,489,447])
    for a in doc:
        mass.append({'id':a.id,'name':a.name,'text':a.text})

    return HttpResponse(json.dumps(mass))



def GetPolitics(request):
    #37,38,16,36,40,39,15,17,20,18,34,58,21,22,23,24,55,52,53,50
    mass=[]
    doc = Doctors.objects.filter(pk__in=[37,16,36,40,39,15,17,20,18,34,58,21,22,23,24,55,52,53,50]).order_by('?')[:4]
    for a in doc:
        mass.append({'id':a.id,'name':a.name,'image':str(a.image1),'work':a.work})

    return HttpResponse(json.dumps(mass))



def MaleFactor(request):
    m_factor = FACTORS.objects.get(type_factors=2)
    return render(request,'male_factor.html',{'content':m_factor})




def FemaleFactor(request):
    m_factor = FACTORS.objects.get(type_factors=1)
    return render(request,'female_factor.html',{'content':m_factor})






def LogoOg(request):
    return render(request,'logo.html')



def Landing(request):
    return render(request,'landing.html')


def error404(request):
    return render(request,'404.html')



#def Robots(request):
#    return render(request,'robots.html')



def PersonalData(request):
    return render(request,'personal-data.html')


def Main(request):

    title_seo = '- Гинекология. Репродуктивный центр. Урологический центр. ЭКО.'
    keywords_seo = 'ЦСМ, Гистероскопия екатеринбург, бесплодие екатеринбург, Гистероскопия, екатеринбург, Миома матки, Полип эндометрия,  Гиперплазия эндометрия, Патология матки, Эндометриоз, Непроходимость маточных труб, Бесплодие, Лечение бесплодия, Мужское бесплодие, Эко, Эко по омс, Спермограмма, Спермограмма екатеринбург, Анализ спермограммы, Где сдать спермограмму,  Гистероскопия, Лапароскопия, внутриматочная инсеминация, ведение беременности, консультация гинеколога, эко по омс, криоконсервация спермы, криоконсервация яйцеклеток, гормональные исследования, клиника эко, гинекологические операции, гинекологические операции екатеринбург'
    description_seo = 'Центр семейной медицины создан в Екатеринбурге в январе 2001 года. Актуальность появления специализированной клиники по лечению бесплодия методами вспомогательных репродуктивных технологий (ВРТ) была обусловлена высоким процентом бесплодных супружеских пар в Уральском регионе и общей мировой тенденцией развития методов лечения бесплодия человека. За годы существования клиники благодаря работе персонала на свет появились более тысячи младенцев, зачатых «в пробирке»'

    images = Slider.objects.all().order_by('sortir')
    counters = Counters.objects.get(id=1)
    return render(request,'index.html', {'pic':images,'title_seo':title_seo,'keywords_seo':keywords_seo,'description_seo':description_seo,'count':counters})




'''
from datetime import datetime
import locale

def GetTestimonials(request):
    r = requests.get('http://www.cfm.ru/manager/systemctl/')
    data = r.json()
    d = {'января': 'январь', 'декабря': 'декабрь','апреля':'апрель','мая':'май','июня':'июнь','июля':'июль','августа':'август','сентября':'сентябрь','октября':'октябрь','ноября':'ноябрь','февраля':'февраль','марта':'март'}

    for a in data:
        if a['date']:

            date_string = a['date']
            locale.setlocale(locale.LC_TIME, "ru_RU")

            for k, v in d.items():
                    date_string = date_string.replace(k, v)

            ru_date_object = datetime.strptime(date_string.strip() , '%d %B %Y').date()

            mass=[]
            doc_arr = a['doc'].split(",")



            print(mass)
            true_doc = mass
            true_date = ru_date_object #date ------------------------------------------->
            true_user = a['user'] #user ------------------------------------------------>
            true_text = a['content']

            for docs in doc_arr:
                doc = Doctors.objects.filter(name=docs).values_list('id',flat=True)
                for m in doc:
                    mass.append(m)
                #    inse = Testimonials(doc=m)
                #    inse.save()

            insert = Testimonials(name=true_user, date=true_date, text=true_text, switch=True)

            insert.save()
    return HttpResponse(0)
'''



def CommentDoc(request,sid):
    doc = Doctors.objects.get(pk=sid)
    comment = Testimonials.objects.filter(doc=sid)

    title_seo = str(doc.name)+'- отзывы о специалистах Центра Семейной Медицины'
    keywords_seo = 'отзывы '+str(doc.name)+' '+str(doc.work)+' Центр Семейной Медицины ЦСМ'
    description_seo = str(doc.name)+', '+str(doc.work)+' Центра Семейной Медицины. Записаться на прием ко врачу или прочитать отзывы пациентов о специалистах ЦСМ на сайте.'

    return render(request,'testimonials-doc.html',{'otz':comment,'doc':doc,'title_seo':title_seo,'description_seo':description_seo,'keywords_seo':keywords_seo})





def StockF(request):
        stock = Stock.objects.filter().order_by('-date')[0:10]
        return render(request,'stock.html',{'news':stock,'title_seo':'- Акции'})





def GetStockF(request,sid):
        stock = Stock.objects.get(id=sid)
        return render(request,'stock-tmp.html',{'stock':stock})



#################
# АНКЕТА
#################
def AnketaF(request):
    return render(request,'anketa.html')




#################
# ДОкторы
#################
def Docktors(request):
    title_seo = '- Наши специалисты'
    description_seo = 'Доктора-врачи Центра Семейной Медицины, это дружный профессиональный коллектив с огромным стажем профессиональной деятельности.'
    doc = Doctors.objects.all().order_by('sortdoc')
    chose = Doctors.CITY_CHOICES
    mass = []
    for a in chose:
        mass.append({'id':a[0],'city':a[1]})
    return render(request,'docktors.html',{'doc':doc,'city':mass,'title_seo':title_seo,'description_seo':description_seo})






def SendEmail(request):
    email = request.GET.get('docemail',False)
    if email:
        return render(request,'send-email.html',{'email':email})





#################
# Фотографии
#################
def PhotosMain(request):
    description_seo = 'Вы можете узнать как выглядит Центр Семейной Медицины изнутри ещё до посещения.'
    photo = Photo.objects.all().order_by('sortir')
    chose = Photo.CITY_CHOICES
    mass = []
    for a in chose:
        mass.append({'id':a[0],'city':a[1]})
    return render(request,'photo.html',{'photo':photo,'city':mass,'title_seo':'- Фотографии клиники. Посмотреть мед кабинеты и покои больницы.','description_seo':description_seo})












#################
# Вопросы
#################
def Questions(request):
    description_seo = 'Вопросы к специалисту по ЭКО, беременности, бесплодию, репродуктивному здоровью.'
    faq = Faq.objects.all()
    return render(request,'faq.html', {'faq':faq,'title_seo':'- Вопросы перед обращением в женскую клинику.','description_seo':description_seo})














#################
# ОТЗЫВЫ
#################
def TestimonialsUsers(request):
    description_seo = 'Узнать отзывы людей о врачах, ведение беременности, успешных эко, о клинике, о Центре Семейной Медицины.'
    otz = Testimonials.objects.filter(switch = True).order_by('-date')[0:5]
    return render(request,'testimonials.html', {'otz':otz,'title_seo':'- Отзывы о Центре Семейной Медицины на Начдива.','description_seo':description_seo})














#API testimonials
def AboutTes(request):
    lm = int(request.GET['limit'])
    otz = Testimonials.objects.filter(switch = True).order_by('-date')[lm:(lm+5)]

    mass = []
    for a in otz:
        mass.append({
        'name':a.name,
        'date':_date(a.date, "d E Y")+' г.',
        'text':a.text,
        })

    return HttpResponse(str(json.dumps(mass)))





def AboutNewsAll(request):
    try:
        if request.COOKIES['sessionid']:
            lm = int(request.GET['limit'])
            otz = News.objects.all().order_by('-date')[lm:(lm+6)]
    except:
            lm = int(request.GET['limit'])
            otz = News.objects.filter(confirm=True).order_by('-date')[lm:(lm+6)]

    mass = []
    for a in otz:
        mass.append({
        'id':a.id,
        'title':a.title,
        'img':str(a.image),
        'description':a.description,
        'date':_date(a.date, "d E Y")+' г.',
        })

    return HttpResponse(str(json.dumps(mass)))




def LastNews(request):
    otz = News.objects.all().order_by('-date')[:3]
    mass = []
    for a in otz:
        mass.append({
        'id':a.id,
        'title':a.title,
        'date':_date(a.date, "d E Y")+' г.',
        })

    return HttpResponse(str(json.dumps(mass)))





def AboutTesKids(request):
    lm = int(request.GET['limit'])
    otz = TestimonialsKids.objects.filter(switch = True).order_by('-date')[lm:(lm+5)]
    mass = []
    for a in otz:
        mass.append({
        'name':a.name,
        'date':_date(a.date, "d E Y")+' г.',
        'text':a.text,
        })

    return HttpResponse(str(json.dumps(mass)))











def FormTestimonials(request):

    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': "6LdayAoTAAAAACkKRJGe-oVrJeXoxukmHCnue29T",
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    ''' End reCAPTCHA validation '''

    print(result,"=========================================================")

    if result['success']:
        pass
    else:
        return redirect('/testimonials/')



    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    date = datetime.now().date()
    insert = Testimonials(name = name,date=date,text=message, switch=False)
    insert.save()

    subject, from_email, to = 'Отзыв', 'yarofeevich@cfm.ru', 'kuskova@cfm.ru'
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_TESTIMONIALS(name,email,message), "text/html")
    msg.send()

    message = 'Спасибо вам за отзыв'

    return render(request,'send_mail.html',{'message':message})






def FormTestimonialsKids(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    date = datetime.now().date()
    insert = TestimonialsKids(name = name,date=date,text=message, switch=False)
    insert.save()

    subject, from_email, to = 'Отзыв детского отделения', 'yarofeevich@cfm.ru', 'kuskova@cfm.ru'
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_TESTIMONIALS(name,email,message), "text/html")
    msg.send()

    message = 'Спасибо вам за отзыв'

    return render(request,'send_mail.html',{'message':message})






def SendEmailForm(request):
    name = request.POST['name']
    post  = request.POST['email']
    message = request.POST['message']
    city = 'Не указано'

    subject, from_email, to = 'Вопрос', 'yarofeevich@cfm.ru', request.POST['doc']
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_FAQ(name,city,post,message,), "text/html")
    msg.send()

    message = 'Спасибо за письмо'

    return render(request,'send_mail.html',{'message':message})





def FormFaq(request):
    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': "6LdayAoTAAAAACkKRJGe-oVrJeXoxukmHCnue29T",
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    ''' End reCAPTCHA validation '''

    print(result,"=========================================================")


    if result['success']:
        pass
    else:
        return redirect('/questions.html/')



    name = request.POST['nameOnline']
    city = request.POST.get('cityOnline',False)
    message = request.POST['messageOnline']
    post  = request.POST['emailOnline']
    insert = Messages(type_message=2,name=name,phone='Отсутствует',post=post,priem='Отсутствует',city=city,message=message,datetime=datetime.now())
    insert.save()

    subject, from_email, to = 'Вопрос', 'yarofeevich@cfm.ru', 'cfm2001@mail.ru' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_FAQ(name,city,post,message,), "text/html")
    msg.send()

    message = 'Спасибо за вопрос'

    return render(request,'send_mail.html',{'message':message})








def FormOnline(request):

    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': "6LdayAoTAAAAACkKRJGe-oVrJeXoxukmHCnue29T",
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    ''' End reCAPTCHA validation '''

    print(result,"=========================================================")

    if result['success']:
        pass
    else:
        return redirect('/online.html/')



    name = request.POST['nameOnline']
    phone = request.POST['phoneOnline']
    post = request.POST['emailOnline']
    if request.POST.get('dateOnline',False) == True:
        date = request.POST['dateOnline']
    else:
        date = '1970-01-01'

    priem = request.POST['dayOnline']
    message = request.POST['messageOnline']
    insert = Messages(type_message=1,name=name,phone=phone,post=post,dateOnline=date,priem=priem,city="Отсутствует",message=message,datetime=datetime.now())
    insert.save()

    insert_record = RecordOnline(name=name,phone=phone,post=post,dateOnline=date,priem=priem,message=message,datetime=datetime.now())

    insert_record.save()

    subject, from_email, to = 'Запись', 'yarofeevich@cfm.ru', 'online_cfm@mail.ru'   #_-------------------------------------------------------------------------------------------------------------------------->
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_ONLINE(name,post,message,phone,date,priem), "text/html")
    msg.send()

    message = 'Ваша запись отправлена'

    return render(request,'send_mail.html',{'message':message})








def FormAnketa(request):

    name = request.POST['nameOnline']
    born = request.POST['bornOnline']
    post  = request.POST['emailOnline']
    phone = request.POST['phoneOnline']
    skype = request.POST['skypeOnline']
    date = request.POST['dateOnline']
    time = request.POST['timeOnline']
    price = request.POST['priceOnline']
    theme  = request.POST['themeOnline']

    subject, from_email, to = 'Запись к психологу', 'yarofeevich@cfm.ru', 'online_cons@cfm.ru'   #_-------------------------------------------------------------------------------------------------------------------------->
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_ANKETA(name,born,post,phone,skype,date,time,price,theme), "text/html")
    msg.send()

    message = 'Ваша заявка принята'
    return render(request,'send_mail.html',{'message':message})





def YandexVert(request):
    return HttpResponse('''<html>
                        <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                        </head>
                        <body>Verification: 6d4cd0571f5eed29</body>
                        </html>''')





def FormCommunicate(request):

    ''' Begin reCAPTCHA validation '''
    recaptcha_response = request.POST.get('g-recaptcha-response')
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
        'secret': "6LdayAoTAAAAACkKRJGe-oVrJeXoxukmHCnue29T",
        'response': recaptcha_response
    }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    ''' End reCAPTCHA validation '''

    print(result,"=========================================================")

    if result['success']:
        pass
    else:
        return redirect('/contacts.html/')


    name = request.POST['nameOnline']
    phone = request.POST['phoneOnline']
    city = request.POST.get('cityOnline',False)
    message = request.POST['messageOnline']
    post  = request.POST['emailOnline']





    insert = Messages(type_message=3,name=name,phone=phone,post=post,priem='Отсутствует',city=city,message=message,datetime=datetime.now())
    insert.save()


    subject, from_email, to = 'Запись', 'yarofeevich@cfm.ru', 'online_cfm@mail.ru'   #_-------------------------------------------------------------------------------------------------------------------------->
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_COM(name,city,post,phone,message), "text/html")
    msg.send()

    message = 'Спасибо за письмо'

    return render(request,'send_mail.html',{'message':message})
