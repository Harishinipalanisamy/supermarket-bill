# # f=open("jill.txt","x")
# # print("fill succes")
import re
f=open("jill.txt","r")
menu=f.read()
import datetime
f=open("jill.txt","w")
x=datetime.datetime.now()
f.write(f"{x}\n")
items=input("enter your iteam:")
x=re.search(items,menu)
print(x)
if x:
    print("yes!!!your item is there")
else:
    print("this counter only avaliable satishnory items")
    
def main():
    
    try:
       items=["pen,rava,maidha"]
       pen=50
       rava=100
       maidha=150
       your_item=input("enter your item:")
       how_many=int(input(f"how many {your_item} you want:"))
       if your_item=="pen":
            total=pen*how_many
            if total>=1000:
                offer_total=total-100
                amt=float(input("enter your amt:"))
                gst=float(input("GST%:"))
                gstamt=amt*gst/100
                f=open("jill.txt","w")
                f.write(f"your total bill is {total}\n")
                f.write(f"if your bill is morethen 1000 rs\n use offertotal is {offer_total}\n")
                f.write(f"GST:{gst}\noffer{offer_total}\n")
                f.write(f"offer bill with GST {offer_total+gstamt}\n")
                print("bill sucess")
            elif your_item=="rava":
                  total=rava*how_many
            if total>=1000:
                offer_total=total-100
                amt=float(input("enter your amt:"))
                gst=float(input("GST%:"))
                gstamt=amt*gst/100
                f=open("jill.txt","w")
                f.write(f"total bill is {total}\n")
                f.write(f"if your bill is morethen 1000 rs\nuse offertotal is {offer_total}\n")
                f.write(f"GST:{gst}\noffer{offer_total}\n")
                f.write(f"offer bill with GST {offer_total+gstamt}\n")
                print("bill sucess")
                
            elif your_item=="maidha":
                total=maidha*how_many
            if total>=1000:
                offer_total=total-100
                amt=float(input("enter your amt:"))
                gst=float(input("GST%:"))
                gstamt=amt*gst/100
                f=open("jill.txt","w")
                f.write(f"total bill is {total}\n")
                f.write(f"if your bill is morethen 1000 rs\nuse offertotal is {offer_total}\n")
                f.write(f"GST:{gst}\noffer{offer_total}\n")
                f.write(f"offer bill with GST {offer_total+gstamt}\n")
                print("bill scuess")
    except: #number ooda error msg kaata ex: ten type pana
           print("plz type number only")
main()
                
import smtplib
import random
def email_sending():
    try:
        receiver_mail=["bhavatharani81@gmail.com","harishinipalanisamy@gmail.com"]
        for i in receiver_mail:
            otp_number=random.randint(0000,9999)
            print(i,otp_number)
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login("harishiniharishini850@gmail.com","wyym nnra klca vovq")
            message=f"your otp number is {otp_number}"
            s.sendmail("harishiniharishini850@gmail.com",i,message)
            s.quit()
            print("mail send succesfully")
    except:   
        print("mail not send")
email_sending()
   




