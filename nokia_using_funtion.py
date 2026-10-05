menu = """
WELCOME
        
Select
    
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert 1
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profile
14. Services
15. SIM services2
0. Turn off
    """


def phone_book_menu():
    print("Phone book")

    phone_book = """
1. Search
2. Service Nos. 1
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign tone
8. Send b’card
9. Options
10. Speed dials
11. Voice tags
0. Back
00. Back to HomePage

                """
    while True:
        print(phone_book)
        phone_book_prompt = input("Choose an option:")
        match (phone_book_prompt):
            case "0" : break
            case "00" : return
            case "1" : print("Search")
            case "2" : print("Service Nos. 1")
            case "3" : print("Add name")
            case "4" : print("Erase")
            case "5" : print("Edit")
            case "6" : print("Copy")
            case "7" : print("Assign tone")
            case "8" : print("Send b’card")
            case "9" :
                print("Options")
                options = """
1. Memory in use
2. Type of view
3. Memory status
0. Back
00. Back to HomePage
                            """
                while True:
                    print(options)
                    options_prompt = input("Choose an option:")
                    match (options_prompt):
                        case "0" : break
                        case "00" : return
                        case "1" : print("Memory in use")
                        case "2" : print("Type of view")
                        case "3" : print("Memory status")
                        case _ : print("Invalid Input")
            case "10" : print("Speed dials")
            case "11" : print("Voice tags")
            case _ : print("Invalid Input")


def messages_menu():
    print("Messages")
    messages = """
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number 4
10. Service command editor
0. Back
00. Back to HomePage
                    """
    while True:
        print(messages)
        messages_prompt = input("Choose an option:")
        match (messages_prompt):
            case "0" : break
            case "00" : return
            case "1" : print("Write messages")
            case "2" : print("Inbox")
            case "3" : print("Outbox")
            case "4" : print("Picture messages")
            case "5" : print("Templates")
            case "6" : print("Smileys")
            case "7" : 
                print("Message settings")
                messages_settings = """
1. Set 12
2. Common 3
0. Back
00. Back to HomePage
                """     
                while True:
                    print(messages_settings)
                    messages_settings_prompt = input("Choose an option:")
                    match (messages_settings_prompt):   
                        case "0" : break
                        case "00" : return
                        case "1" : 
                            print("Set 12")
                            set_1 = """
1. Message centre number
2. Messages sent as
3. Message validity
0. Back
00. Back to HomePage
                                        """
                            while True:
                                print(set_1)
                                set_1_prompt = input("Choose an option:")
                                match (set_1_prompt):
                                    case "0" : break
                                    case "00" : return
                                    case "1" : print("Message centre number")
                                    case "2" : print("Messages sent as")
                                    case "3" : print("Message validity")
                                    case _ : print("Invalid Input")
                        case "2" :    
                            print("Common 3")
                            common_3 = """
1. Delivery reports
2. Reply via same centre
3. Character support
0. Back
00. Back to HomePage
                                        """
                            while True:
                                print(common_3)
                                common_3_prompt = input("Choose an option:")
                                match (common_3_prompt):
                                    case "0" : break
                                    case "00" : return
                                    case "1" : print("Delivery reports")
                                    case "2" : print("Reply via same centre")
                                    case "3" : print("Character support")
                                    case _ : print("Invalid Input")
                        case _ : print("Invalid Input")
            case "8" : print("Info service")
            case "9" : print("Voice mailbox number 4")
            case "10" : print("Service command editor")
            case _ : print("Invalid Input")      


def call_register_menu():
    print("Call register")
    call_register = """
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
0. Back
00. Back to HomePage
        """
    while True:
        print(call_register)
        call_register_prompt = input("Choose an option:")
        match (call_register_prompt):
            case "0" : break
            case "00" : return
            case "1" : print("Missed calls")
            case "2" : print("Received calls")
            case "3" : print("Dialled numbers")
            case "4" : print("Erase recent call lists")
            case "5" : 
                print("Show call duration")
                show_call_duration = """
1. Last call duration
2. All calls’ duration
3. Received calls’ duration
4. Dialled calls’ duration
5. Clear timers
0. Back
00. Back to HomePage
                            """
                while True:
                    print(show_call_duration)
                    show_call_duration_prompt = input("Choose an option:")
                    match (show_call_duration_prompt):
                        case "0" : break
                        case "00" : return
                        case "1" : print("Last call duration")
                        case "2" : print("All calls’ duration")
                        case "3" : print("Received calls’ duration")
                        case "4" : print("Dialled calls’ duration")
                        case "5" : print("Clear timers")
                        case _ : print("Invalid Input")        
            case "6" : 
                print("Show call costs")
                show_call_costs = """
1. Last call cost
2. All calls’ cost
3. Clear counters
0. Back
00. Back to HomePage
                            """
                while True:
                    print(show_call_costs)
                    show_call_costs_prompt = input("Choose an option:")
                    match (show_call_costs_prompt):
                        case "0" : break
                        case "00" : return
                        case "1" : print("Last call cost")
                        case "2" : print("All calls’ cost")
                        case "3" : print("Clear counters")
                        case _ : print("Invalid Input")
            case "7" : 
                print("Call cost settings")
                call_cost_settings = """
1. Call cost limit
2. Show costs in
0. Back
00. Back to HomePage
                            """
                while True:
                    print(call_cost_settings)
                    call_cost_settings_prompt = input("Choose an option:")
                    match (call_cost_settings_prompt):
                        case "0" : break
                        case "00" : return
                        case "1" : print("Call cost limit")
                        case "2" : print("Show costs in")
                        case _ : print("Invalid Input")
            case "8" : print("Prepaid credit")
            case _ : print("Invalid Input")


def tones_menu():
    print("Tones")
    tones = """
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
0. Back
00. Back to HomePage
        """
    while True:
        print(tones)
        tones_prompt = input("Choose an option:")
        match (tones_prompt):
            case "0" : break
            case "00" : return
            case "1" : print("Ringing tone")
            case "2" : print("Ringing volume")
            case "3" : print("Incoming call alert")
            case "4" : print("Message alert tone")
            case "5" : print("Keypad tones")
            case "6" : print("Warning tones")
            case "7" : print("Vibrating alert")
            case "8" : print("Screen saver")
            case _ : print("Invalid Input")


def settings_menu():
    print("Settings")
    settings = """
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
0. Back
00. Back to HomePage
        """
    while True:
        print(settings)
        settings_prompt = input("Choose an option:")
        match (settings_prompt):
            case "0" : break
            case "00" : return
            case "1" : 
                print("Call settings")
                call_settings = """
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer 1
0. Back
00. Back to HomePage
            """
                while True:
                    print(call_settings)
                    call_settings_prompt = input("Choose an option:")
                    match (call_settings_prompt):
                        case "0" : break
                        case "00" : return
                        case "1" : print("Automatic redial")
                        case "2" : print("Speed dialling")
                        case "3" : print("Call waiting options")
                        case "4" : print("Own number sending")
                        case "5" : print("Phone line in use")
                        case "6" : print("Automatic answer 1")
                        case _ : print("Invalid Input")
            case "2" : 
                print("Phone settings")
                phone_settings = """
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
0. Back
00. Back to HomePage
            """
                while True:
                    print(phone_settings)
                    phone_settings_prompt = input("Choose an option:")
                    match (phone_settings_prompt):
                        case "0" : break
                        case "00" : return
                        case "1" : print("Language")
                        case "2" : print("Cell info display")
                        case "3" : print("Welcome note")
                        case "4" : print("Network selection")
                        case "5" : print("Confirm SIM service actions")
                        case _ : print("Invalid Input")
            case "3" : 
                print("Security settings")
                security_settings = """
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes1
0. Back
00. Back to HomePage
            """
                while True:
                    print(security_settings)
                    security_settings_prompt = input("Choose an option:")
                    match (security_settings_prompt):
                        case "0" : break
                        case "00" : return
                        case "1" : print("PIN code request")
                        case "2" : print("Call barring service")
                        case "3" : print("Fixed dialling")
                        case "4" : print("Closed user group")
                        case "5" : print("Security level")
                        case "6" : print("Change access codes1")
                        case _ : print("Invalid Input")
            case "4" : print("Restore factory settings")
            case _ : print("Invalid Input")


def music_menu():
    print("Music")
    music = """
1. Music player
2. Radio
3. Recorder
4. Track list
0. Back
00. Back to HomePage
        """
    while True:
        print(music)
        music_prompt = input("Choose an option:")
        match (music_prompt):
            case "0" : break
            case "00" : return
            case "1" : print("Music player")
            case "2" : print("Radio")
            case "3" : print("Recorder")
            case "4" : print("Track list")
            case _ : print("Invalid Input")


def clock_menu():
    print("Clock")
    clock = """
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
0. Back
00. Back to HomePage
        """
    while True:
        print(clock)
        clock_prompt = input("Choose an option:")
        match (clock_prompt):
            case "0" : break
            case "00" : return
            case "1" : print("Alarm clock")
            case "2" : print("Clock settings")
            case "3" : print("Date setting")
            case "4" : print("Stopwatch")
            case "5" : print("Countdown timer")
            case "6" : print("Auto update of date and time")
            case _ : print("Invalid Input")


while True:
    print(menu)

    menu_prompt = input("Choose an option:") 

    match (menu_prompt):
        case "0" : break
        case "1" : phone_book_menu()
        case "2" : messages_menu()
        case "3" : print("Chat")
        case "4" : call_register_menu()
        case "5" : tones_menu()
        case "6" : settings_menu()
        case "7" : print("Call divert 1")
        case "8" : music_menu()
        case "9" : print("Games")
        case "10" : print("Calculator")
        case "11" : print("Reminders")
        case "12" : clock_menu()
        case "13" : print("Profile")
        case "14" : print("Services")
        case "15" : print("SIM services2")
        case _ : print("Invalid Input")
