# TG-AutoReport-scheduled

If you would like to stop diversion groups in Ukraine (which are paid to mark buildings for bombings, reporting UKR soldier positions and other disinformation)
Follow these steps to auto-report them in Telegram

SOURCE AND AUTHOR https://github.com/NoImN0t/TG-AutoReport/

## Due to high demand see TROUBLESHOOTING section (error: [420 FLOOD_WAIT_X])

## FIRST TIME SETUP
1. Get telegram app on your phone (Google Play store)
2. Login to it (if first time use: follow in app instructions, allow permissions, validate phone number) 	 	 	 
3. Download and extract TG-AutoReport-scheduled-main.zip
4. Launch TG-autoreport-scheduled.exe
5. Enter your phone number (+370 xxx xxxxx)
<img align="left" src="https://user-images.githubusercontent.com/20355306/156067187-c1b02ce7-3eb3-4a01-a6d7-02cf802df61e.png"/>
<br clear="left"/>
6. Confirm it press “Y” and Enter. You will receive **confirmation code to your phone** 
<br clear="left"/>
7. Enter confirmation code to console
<img align="left" src="https://user-images.githubusercontent.com/20355306/156067187-c1b02ce7-3eb3-4a01-a6d7-02cf802df61e.png"/> 
<br clear="left"/>
9.App is now configured! (two session files will appear in directory)

## SCHEDULE TASK
It will create task scheduler task to run every 4 hours (taskschd.msc)
1. Launch SetSchedule.bat

## DELETE SCHEDULE TASK
1. Launch RemoveSchedule.bat

## RUN MANUALY
1. Launch TG-autoreport-scheduled.exe

# TROUBLESHOOTING

 If you are getting this error:
 Telegram says: [420 FLOOD_WAIT_X] - A wait of 22719 seconds is required (caused by "contacts.ResolveUsername")
 Please go to: https://my.telegram.org/
<img align="left" src="https://user-images.githubusercontent.com/20355306/156343544-5b149ff4-5087-4d16-9427-8687b0cfb329.png"/>
<br clear="left"/>
 Create new APP (or use existing)
<img align="left" src="https://user-images.githubusercontent.com/20355306/156343997-80a8ff4a-a4ab-429f-8c37-d88aa259d5a1.png"/>
<br clear="left"/>
 and add these values to .env file
<img align="left" src="https://user-images.githubusercontent.com/20355306/156344351-eb5aebef-4545-4936-8531-f8e7d6154320.png"/>
<br clear="left"/>


## IN ACTION
<img align="left" src="https://user-images.githubusercontent.com/20355306/156218573-84ca45b9-00b3-4a34-b40e-c05fc14e7b27.PNG"/> 
<p align="left">

live ban list: https://docs.google.com/spreadsheets/d/1ovusoIost6DZt5dwGWWMPRndtLWe-7zoAsbdeo9aK5A/edit#gid=0

extra: to change or get new .env go to https://my.telegram.org/auth

src compiled with auto-py-to-exe
</p>
