from django.shortcuts import render
from events.models import events,participate
from django.core.mail import EmailMessage
from datetime import datetime
from django.shortcuts import redirect



# Create your views here.

def sendMsg(contact_no,message_str):
    from twilio.rest import Client
    contact_no = contact_no.replace(' ','')
    contact_no = contact_no.replace('-','')
    contact_no = contact_no.replace('+91','')
    contact_no = '+91'+contact_no
    account_sid = ('twilio_SID')
    auth_token = ('twilio auth token')
    client = Client(account_sid, auth_token)
    client.messages.create(from_='your twilio number',
                        to=contact_no,
                        body=message_str)



def participate_reg(request):
    if request.method == "POST":
        allEvents = events.objects.values('id','event_name','venue','from_Date')
        name = request.POST.get('name')
        contact_no = request.POST.get('contact_no')
        email_id = request.POST.get('email_id')
        registeration_type = request.POST.get('registeration_type')
        event = int(request.POST.get('event'))
        no_of_people = request.POST.get('no_of_people')
        if not no_of_people:
            no_of_people = 1
        f = open("participate_cnt.txt",'r')
        cnt = int(f.read())
        f.close()
        cnt+=1
        f = open("participate_cnt.txt",'w')
        f.write(str(cnt))
        f.close()
        p1 = participate(cnt,name,contact_no,email_id,registeration_type,event,no_of_people)
        p1.save()
        for i in allEvents:
            if i['id'] == event:
                eventName = i['event_name']
                eventVenue = i['venue']
                eventstart = i['from_Date']
        message_str = "Greetings, Mr./Ms./Miss. "+str(name)+"\nThankyou for regestering in the event " + str(eventName) +"\nSee you soon at : "+str(eventVenue)+" on : " + str(eventstart)
        to_email = []
        to_email.append(email_id)
        title = 'Participation in ' + str(eventName)
        # email = EmailMessage(title, message_str, to=to_email)
        # email.send()
        # sendMsg(contact_no,message_str)

    response = redirect('/home/')
    return response

def event_reg(request):
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        description = request.POST.get('description')
        venue = request.POST.get('venue')
        fdate = str(request.POST.get('fromDate_0')) + " "+ str(request.POST.get('fromDate_1'))
        tdate = str(request.POST.get('toDate_0')) + " "+ str(request.POST.get('toDate_1'))
        deadline_date = str(request.POST.get('Deadline_0')) + " "+ str(request.POST.get('Deadline_1'))
        hostemail = request.POST.get('hostemail')
        hostpassword = request.POST.get('hostpassword')
        format = '%Y-%m-%d %H:%M:%S'
        from_Date = datetime.strptime(fdate, format)
        to_Date = datetime.strptime(tdate, format)
        Deadline = datetime.strptime(deadline_date, format)
        f = open("event_cnt.txt",'r')
        cnt = int(f.read())
        f.close()
        cnt+=1
        f = open("event_cnt.txt",'w')
        f.write(str(cnt))
        f.close()
        e1 = events(cnt,event_name,description,venue,from_Date,to_Date,Deadline,hostemail,hostpassword)
        e1.save()
        to_email = []
        to_email.append(hostemail)
        message_str = "Thank you for registering your Event please verify your event details \n\nEvent Name :  "+event_name + "\nVenue at : "+venue + "\nFrom " + fdate + "\nTo : " + tdate + "\nDeadline for Registeration : " + deadline_date + "\n\n\nThanks and Regards \nReniz Shah"
        # email = EmailMessage('Event Registration', message_str, to=to_email)
        # email.send()
    response = redirect('/home/')
    return response

def index(request):
    return render(request,'events/index.html')
    
def allEvents(request):
    allEvents = events.objects.values()
    alleventsList = []
    for i in allEvents:
        dic = {'id':i['id'],
            'name':i['event_name'],
            'description' : i['description'],
            'venue' : i['venue'],
            'from_Date' : i['from_Date'],
            'to_Date' : i['to_Date'],
            'Deadline' : i['Deadline'],
            'host_email' : i['host_email'],
            }
        alleventsList.append(dic)
    params = {'events':alleventsList}

    return render(request,'events/allEvents.html',params)
    



def register_event(request):
    return render(request,'events/register_event.html')


def register_participate(request):
    allEvents = events.objects.values('id','event_name','Deadline')
    alleventsList = []
    format = '%Y-%m-%d %H:%M:%S'
    for i in allEvents:
        deadline = str(i['Deadline'])
        deadline = deadline[:-6]
        Deadline = datetime.strptime(deadline, format)
        if Deadline > datetime.now():
            dic = {'id':i['id'] , 'name':i['event_name']}
            alleventsList.append(dic)
    params = {'events':alleventsList}
    return render(request,'events/register_participate.html',params)


def dashboard(request):
    params={}
    if request.method == "POST":
        passwordMatch = False
        event_id = int(request.POST.get('event_id'))
        hostpassword = request.POST.get('hostpassword')
        allEvents = events.objects.values()
        allparticipates = participate.objects.values()
        for event in allEvents:
            if event['id'] == event_id:
                if event['host_password'] == hostpassword:
                    event_name = event['event_name']
                    passwordMatch = True
        if passwordMatch:
            participatesList = []
            for participates in allparticipates:
                if participates['event_id'] == event_id:
                    dic = {'id':participates['id'],
                    'name' : participates['name'],
                    'contact_no' : participates['contact_no'],
                    'email_id' : participates['email_id'],
                    'event' : event_name,
                    'no_of_people' : participates['no_of_people'],}
                    participatesList.append(dic)
            params = {'data':participatesList}


    return render(request,'events/dashboard.html',params)
