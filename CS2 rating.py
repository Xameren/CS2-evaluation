from datetime import datetime
import time
import sys
import json
import os
os.system("title " + "Xameren's CS2 evaluation script")

Kills = 0
Deaths = 0  
Assists = 0
HS = 0
WR = 0
Damage = 0

TotalTotalRating = 0
TotalKillRating = 0
TotalAssistRating = 0
TotalHSrating = 0
TotalDamageRating = 0

Rounds = 0
Matches = 0
Wins = 0
Draws = 0
Losses = 0

SaveFile = "Savefile.json"
GameList = []

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

def rating(Newkills, NewDeaths, NewAssists, NewHS, NewDamage, NewRounds, NewWin, AddMatchTotal, MatchDate = "N/A"):
    global TotalRating, Rounds, Kills, Deaths, Assists, HS, Damage, Matches, TotalAssistRating, TotalDamageRating, TotalHSrating,TotalKillRating, GameList, TotalTotalRating, Wins, Draws, Losses
    KillRating = round((Newkills/NewDeaths)/2, 3)
    AssistRating = round(NewAssists/8, 3)
    HSrating = round(NewHS/100, 3)
    DamageRating = NewDamage/(135*NewRounds)

    KillRating = min(Newkills/(NewRounds*1.25), 1)*0.4+min((Newkills/NewDeaths)/1.25, 1)*0.4-min(NewDeaths/NewRounds, 1)*0.2
    AssistRating= min(NewAssists/(NewRounds*0.5), 1)*0.6+min(NewAssists/(NewAssists+Newkills), 1)*0.4
    HSrating = NewHS/100*0.6+min(NewHS/100*Newkills/Newkills, 1)*0.4
    DamageRating = min(NewDamage/(NewRounds*125), 1)*0.5+min(Newkills/(NewRounds*1.25), 1)*0.3+min(NewDamage/Newkills/125, 1)*0.2
    
    if AddMatchTotal:
        MatchDate = datetime.now().strftime("%d/%m/%Y")

    if NewWin == "y":
        Wins += 1
    elif NewWin == "draw":
        Draws += 1
    elif NewWin == "n":
        Losses += 1

    if KillRating > 1:
        KillRating = 1
    if AssistRating > 1:
        AssistRating = 1
    if HSrating > 1:
        HSrating = 1
    if DamageRating > 1:
        DamageRating = 1
    
    TotalRating = KillRating*0.3+DamageRating*0.3+HSrating*0.2+AssistRating*0.2


    if AddMatchTotal:
        Kills += Newkills
        Deaths += NewDeaths
        Assists += NewAssists
        HS += NewHS
        Damage += NewDamage
        Rounds += NewRounds
        TotalAssistRating += AssistRating
        TotalDamageRating += DamageRating
        TotalHSrating += HSrating
        TotalKillRating += KillRating
        TotalTotalRating += 0.4*KillRating+0.3*DamageRating+0.2*HSrating+0.1*AssistRating
        
        Matches += 1

        TotalTotalRating = 0.4*TotalKillRating+0.3*TotalDamageRating+0.2*TotalHSrating+0.1*TotalAssistRating
        

        GameList.insert(0, f"K: {Newkills}, D: {NewDeaths}, A: {NewAssists}, HS: {NewHS}, DMG: {NewDamage}, Rounds: {NewRounds}, Win: {NewWin}, Date: {MatchDate}")
    matchstats(Newkills, NewDeaths, NewAssists, NewHS, NewDamage, NewRounds, NewWin, AssistRating, HSrating, KillRating, DamageRating, TotalRating, MatchDate)

def register():
    global Username, Kills, Deaths, Assists, HS, Damage, Matches, WR
    reset = True
    while reset:
        print("Welcome to xameren's CS2 evaluation tool")
        print("What's your Username?")
        Username = input("Your Username:")
        print("Do you want to import your stats?")
        print("You will be prompted to fill your KD, kills, assists, deaths, HS% and damage from your last round")
        while True:
            fillornot = input("(y/n) ")
            if fillornot.lower() == "y":
                while True:
                    try:    
                        Ki = int(input("Kills: "))
                        De = int(input("Deaths: "))
                        As = int(input("Assists: "))
                        Hs = int(input("HS%: "))
                        Da = int(input("Damage: "))
                        Ro = int(input("Rounds: "))
                        while True:
                            Wi = input("Did you win? (y/draw/n)").lower()
                            if Wi == "y" or Wi == "n" or Wi == "draw":
                                break
                        break
                    except ValueError:
                        print("Please enter valid numbers")
                correctregister = input("Is this all correct? (y/N) ").lower()
                if correctregister == "y":
                    reset = False
                    rating(Ki, De, As, Hs, Da, Ro, Wi, AddMatchTotal = True)
                    break
            elif fillornot.lower() == "n":
                print("Alright, no problem")
                reset = False
                time.sleep(1)
                break

def WRcalc():
    if Losses == 0:
        return 100
    else:
        return round((Wins/Matches)*100, 2)


def Coloring(numbah):
    if numbah < 33:
        return RED
    elif numbah < 66:
        return YELLOW
    else:
        return GREEN
def ColoringLow(numbah):
    if numbah < 33:
        return GREEN
    elif numbah < 66:
        return YELLOW
    else:
        return RED
    
def matchstats(Newkills, NewDeaths, NewAssists, NewHS, NewDamage, NewRounds, NewWin, AssistRating, HSrating, KillRating, DamageRating, TotalRating, MatchDate = "N/A"):
    Newkills = int(Newkills)
    NewDeaths = int(NewDeaths)
    NewAssists = int(NewAssists)
    NewHS = int(NewHS)
    NewDamage = int(NewDamage)
    NewRounds = int(NewRounds)
    
    print("\033[H\033[J", end="")
    print("Match rating")
    print(f" Name: {Username}")
    print(f" Date: {MatchDate}")
    print(f" Match {f"{GREEN}Won" if NewWin == "y" else f"{RED}Lost" if NewWin == "n" else "Drawn"}{END}")
    print(f" Rounds: {NewRounds}")
    spaces = "                                  "
    print()
    print(f"{Coloring(TotalRating*100)}XMRating: {round(TotalRating*100, 3)}{END}")
    print(f"{Coloring(HSrating*100)}{spaces}HS rating:    {round(HSrating*100, 3)}{END}")
    print(f"{Coloring(AssistRating*100)}{spaces}Assist rating {round(AssistRating*100, 3)}{END}")
    print()

    print(f"{spaces}Headshots:")
    print(f"{Coloring((NewHS/100*Newkills)/12*100)}{spaces}Total: {round(NewHS/100*Newkills, 3)}{END}")
    print(f"{Coloring((NewHS/100*Newkills/NewRounds)/1*100)}{spaces}Headshots/Round: {round(NewHS/100*Newkills/NewRounds, 3)}{END}")
    print(f"{Coloring(NewHS)}{spaces}Headshot%:       {NewHS}{END}")
    print()
    print(f"{spaces}Damage:")
    print(f"{Coloring(NewDamage/(NewRounds*130)*100)}{spaces}Total: {NewDamage}{END}")
    print(f"{Coloring(NewDamage/(NewRounds*130)*100)}{spaces}Average/Round: {round(NewDamage/NewRounds, 3)}{END}")
    print(f"{Coloring((NewDamage/Newkills)/125*100)}{spaces}Average/Kill: {round(NewDamage/Newkills, 3)}")
    print()
    print("\033[H", end="")
    print("\n\n\n\n\n")
    print()
    print(f"{Coloring(round(KillRating*100, 3))}  Kill rating:   {round(KillRating*100, 3)}{END}")
    print(f"{Coloring(round(DamageRating*100, 3))}  Damage rating: {round(DamageRating*100, 3)}{END}")
    print()
    print(f"Kills:")
    print(f"{Coloring(Newkills/NewRounds*100)}Total: {Newkills}{END}")
    print(f"{Coloring(Newkills/NewRounds*100)}Average/Round: {round(Newkills/NewRounds, 3)}{END}")
    print(f"{Coloring((Newkills/NewDeaths)/1.2*100)}K/D: {round(Newkills/NewDeaths, 3)}{END}")
    print()
    print("Deaths:")
    print(f"{ColoringLow(NewDeaths/NewRounds*100)}Total: {NewDeaths}{END}")
    print(f"{ColoringLow(NewDeaths/NewRounds*100)}Deats/Round: {round(NewDeaths/NewRounds, 3)}{END}")
    print()
    print("Assists:")
    print(f"{Coloring(NewAssists/NewRounds/1*100)}Total: {NewAssists}{END}")
    print(f"{Coloring(NewAssists/NewRounds/1*100)}Assists/Round {round(NewAssists/NewRounds, 3)}{END}")
    input("\nPress enter to exit")


def profile():
    global Username, Matches, Kills, HS, Rounds, Damage, Deaths, Assists
    while True:

        """
    TotalAssistRating += AssistRating
    TotalDamageRating += DamageRating
    TotalHSrating += HSrating
    TotalKillRating += KillRating
        """

        print("\033[H\033[J", end="")
        print(f"Name: {Username}")
        print()
        try:
            TotalTotalRating = round(0.4*(round(TotalKillRating/Matches*100, 3))+0.3*(round(TotalDamageRating/Matches*100, 3))+0.2*(round(TotalHSrating/Matches*100, 3))+0.1*(round(TotalAssistRating/Matches*100, 3)), 3)
            print("\033[H\033[J", end="")
            print(f"Name: {Username}")
            print()
            print(f"{Coloring(TotalTotalRating)}XMRating: {TotalTotalRating}{END}")
            print(f"\n\n\n\n\n\n\n\n\n\n                                                      Draws:   {Draws} \n                                                      Matches: {Matches}")
            spaces = "                                  "
            print("\033[H", end="")
            print(f"Name: {Username}")
            print()
            print(f"{Coloring(TotalTotalRating)}XMRating: {TotalTotalRating}{END}")
            print(f"{Coloring(round(TotalHSrating/Matches*100, 3))}                              HS rating:     {round(TotalHSrating/Matches*100, 3)}{END}")
            print(f"{Coloring(round(TotalAssistRating/Matches*100, 3))}                              Assist rating: {round(TotalAssistRating/Matches*100, 3)}{END}")
            print("")
            print(f"{spaces}Headshots:")
            print(f"{spaces}  Total:          {round(Kills*((HS/Matches)/100), 0)}")
            print(f"{Coloring(round(Kills*(HS/Matches/100)/Matches, 2)/20*100)}{spaces}  Average/Match:  {round(Kills*(HS/Matches/100)/Matches, 2)}{END}")
            print(f"{Coloring(round(Kills*(HS/Matches/100)/Rounds, 2)/1*100)}{spaces}  Average/Round:  {round(Kills*(HS/Matches/100)/Rounds, 2)}{END}")
            print(f"{Coloring(round(HS/Matches))}{spaces}  Average%:       {round(HS/Matches)}%{END}")
            print()
            print(f"{spaces}Games:")
            print(f"{spaces}  Wins:   {Wins}") 
            print(f"{Coloring(WRcalc()/75*100)}{spaces}  WR%:    {WRcalc()}%{END}") 
            print(f"{spaces}  Rounds: {Rounds}")
            print("\n")
            print(f"{spaces}Damage:")
            print(f"{spaces}  Total:          {Damage}") 
            print(f"{Coloring(round(Damage/Matches, 2)/(130*(Rounds/Matches))*100)}{spaces}  Average/Match:  {round(Damage/Matches, 2)}{END}") 
            print(f"{Coloring(round(Damage/Rounds, 2)/130*100)}{spaces}  Average/Round:  {round(Damage/Rounds, 2)}{END}")  
            print(f"{Coloring(round((Damage/(Kills*125)*100), 2))}{spaces}  Average/Kill:  {round(Damage/Kills, 2)}{END}") 

            print("\033[H", end="")
            print(f"Name: {Username}")
            print()
            print(f"{Coloring(TotalTotalRating)}XMRating: {TotalTotalRating}{END}")
            print(f"{Coloring(round(TotalKillRating/Matches*100, 3))}  Kill rating:   {round(TotalKillRating/Matches*100, 3)}{END}")
            print(f"{Coloring(round(TotalDamageRating/Matches*100, 3))}  Damage rating: {round(TotalDamageRating/Matches*100, 3)}{END}")
            print("")
            print(f"Kills:")
            print(f"  Total:         {Kills}")
            print(f"  {Coloring(round(Kills/Matches, 2)/25*100)}Average/Match: {round(Kills/Matches, 2)}{END}")
            print(f"  {Coloring(round(round(Kills/Rounds, 2))/1.5*100)}Average/Round: {round(Kills/Rounds, 2)}{END}")
            print(f"  {Coloring(round(Kills/Deaths, 2)/1.5*100)}K/D:           {round(Kills/Deaths, 2)}{END}")
            print()
            print(f"Deaths:")
            print(f"  Total:   {Deaths}") 
            print(f"  {ColoringLow(round(Deaths/Matches, 2)/22*100)}Average/Match: {round(Deaths/Matches, 2)}{END}") 
            print(f"  {ColoringLow(round(Deaths/Rounds, 2)/1*100)}Average/Round: {round(Deaths/Rounds, 2)}{END}") 
            print("\n")
            print(f"Assists:")
            print(f"  Total:   {Assists}")
            print(f"  {Coloring(round(Assists/Matches, 2)/8*100)}Average/Match: {round(Assists/Matches, 2)}{END}")
            print(f"  {Coloring(round(Assists/Rounds, 2)/0.4*100)}Average/Round: {round(Assists/Rounds, 2)}{END}")
            print("\n")
        except Exception as e:
            print("error ", e)
            print("There are no stats to judge you... yet.")
        print("c) Change username")
        print("r) Recent matches")
        print("q) Back to the main menu")
        inputprofile = input().lower()
        if inputprofile == "c":
            newuser = input("Your new Username will be: ")
            Username = newuser
        elif inputprofile == "xamseccod":
                print("eGFtZXJlbiBtYWRlIHRoaXM=")
        elif inputprofile == "r":
            page = 0
            while True:
                print("\033[H\033[J", end="")
                print("Recent matches\n")
                for i, item in enumerate(GameList[0+(page*15):15+(page*15)]):
                    Colormatches = GameList[i]
                    values = dict(stritem.split(": ") for stritem in Colormatches.split(", "))
                    if values["Win"] == "y":
                        print(f" {GREEN}Match {int(i)+(page*15)+1} - {item}{END}")
                    elif values["Win"] == "n":
                        print(f" {RED}Match {int(i)+(page*15)+1} - {item}{END}")
                    else:
                        print(f" Match {int(i)+(page*15)+1} - {item}")


                print(f"\n1 - {len(GameList)}) to view a match")
                if len(GameList) > 15:
                    if page*15+15 < len(GameList):
                        print(f"\nShowing {page*15+1} - {page*15+15} out of {len(GameList)} matches\n")
                    else:
                        print(f"\nShowing {page*15+1} - {len(GameList)} out of {len(GameList)} matches\n")
                    print("b) Previous page\nn) Next page")

                
                print("h) Help")
                print("q) Back to menu")


                leaveinput = input()
# Newkills, NewDeaths, NewAssists, NewHS, NewDamage, NewRounds, NewWin, AddMatchTotal

                try:
                    Getstats = int(leaveinput)
                    if 1 <= Getstats <= len(GameList):
                        Getstats -= 1
                        DeletedMatch = GameList[Getstats]
                        values = dict(stritem.split(": ") for stritem in DeletedMatch.split(", "))
                        try:
                            rating(int(values["K"]), int(values["D"]), int(values["A"]), int(values["HS"]), int(values["DMG"]), int(values["Rounds"]), values["Win"], False, values["Date"])
                        except Exception:
                            rating(int(values["K"]), int(values["D"]), int(values["A"]), int(values["HS"]), int(values["DMG"]), int(values["Rounds"]), values["Win"], False)

                except Exception:
                    if leaveinput == "q":
                        break
                    elif leaveinput == "n":
                        if len(GameList) > page*15+15:
                            page += 1
                        else:
                            print("This is the last page.")
                    elif leaveinput == "b":
                        if 0+(page*15) > 0:
                            page -= 1
                        else:
                            print("This is the first page.")
                    if leaveinput == "h":
                        print("\033[H\033[J", end="")
                        print("Help")
                        print(" K   - Kills")
                        print(" D   - Deaths")
                        print(" A   - Assists")
                        print(" HS  - Headshot percentage")
                        print(" DMG - Damage dealt")
                        print(" Win - If you won (y), lost (n), or tied (draw)")
                        print("Enter anything to exit")
                        input()
        elif inputprofile == "q":
            break

def addmatch():
    Quit = False
    while True:
        print("\033[H\033[J", end="")
        print("Adding a match")
        print("Please put in your statistics of the match")
        try:
            Newkills = int(input("Kills: "))
            NewDeaths = int(input("Deaths: "))
            NewAssists = int(input("Assists: "))
            NewHS = int(input("HS%: "))
            NewDamage = int(input("Damage: "))
            NewRounds = int(input("Rounds: "))
            while True:
                WINyn = input("Did you win? (y/draw/n) ").lower()
                if WINyn == "n" or WINyn == "y" or WINyn == "draw":
                    NewWin = WINyn
                    break

            matchsure = input("Is this all correct? (y/n) ").lower()
            if matchsure == "y":
                break
            elif matchsure == "n":
                Quit = True
                break
        except ValueError:
            print("Please only provide a number")
    if not Quit:
        rating(Newkills, NewDeaths, NewAssists, NewHS, NewDamage, NewRounds, NewWin, True)

def removematch():
    global Kills, Deaths, Assists, HS, Damage, Rounds, Wins, Losses, Draws, Matches, TotalKillRating, TotalAssistRating, TotalHSrating, TotalDamageRating
    print("\033[H\033[J", end="")
    page = 0
    while True:
        print("\033[H\033[J", end="")
        print("Which match would you like to remove?\n")
        for i, item in enumerate(GameList[0+(page*15):15+(page*15)]):
            
            Colormatches = GameList[i]
            values = dict(stritem.split(": ") for stritem in Colormatches.split(", "))
            if values["Win"] == "y":
                print(f" {GREEN}Match {int(i)+(page*15)+1} - {item}{END}")
            elif values["Win"] == "n":
                print(f" {RED}Match {int(i)+(page*15)+1} - {item}{END}")
            else:
                print(f" Match {int(i)+(page*15)+1} - {item}")
        if page*15+15 < len(GameList):
            print(f"\nShowing {page*15+1} - {page*15+15} out of {len(GameList)} matches\n")
        else:
            print(f"\nShowing {page*15+1} - {len(GameList)} out of {len(GameList)} matches\n")
        print(f"1 - {len(GameList)}) to remove a match")
        print("b) Previous page")
        print("n) Next page")
        print("q) Exit to the main menu")
        Chosen1 = input()
        try:
            a = 5
            Chosen = int(Chosen1)
            if 1 <= Chosen <= len(GameList):
                Chosen -= 1
                DeletedMatch = GameList[Chosen]
                values = dict(stritem.split(": ") for stritem in DeletedMatch.split(", "))
                Kills -= int(values["K"])
                Deaths -= int(values["D"])
                Assists -= int(values["A"])
                HS -= int(values["HS"])
                Damage -= int(values["DMG"])
                Rounds -= int(values["Rounds"])
                Matches -= 1

                if values["Win"] == "y":
                    Wins -= 1
                elif values["Win"] == "n":
                    Losses -= 1
                elif values["Win"] == "draw":
                    Draws -= 1
                    
                    """
                    
                    
    KillRating = min(Newkills/(NewRounds*1.25), 1)*0.4+min((Newkills/NewDeaths)/1.25, 1)*0.4-min(NewDeaths/NewRounds, 1)*0.2
    AssistRating= min(NewAssists/(NewRounds*0.5), 1)*0.6+min(NewAssists/(NewAssists+Newkills), 1)*0.4
    HSrating = NewHS/100*0.6+min(NewHS/100*Newkills/Newkills, 1)*0.4
    DamageRating = min(NewDamage/(NewRounds*125), 1)*0.5+min(Newkills/(NewRounds*1.25), 1)*0.3+min(NewDamage/Newkills/125, 1)*0.2


                    """
                Newkills = int(values["K"])
                NewDeaths = int(values["D"])
                NewAssists = int(values["A"])
                NewRounds = int(values["Rounds"])
                NewHS = int(values["HS"])
                NewDamage = int(values["DMG"])



                if round(round(min(Newkills/(NewRounds*1.25), 1)*0.4+min((Newkills/NewDeaths)/1.25, 1)*0.4-min(NewDeaths/NewRounds, 1)*0.2, 3)/2, 3) < 1:
                    TotalKillRating -= round(min(Newkills/(NewRounds*1.25), 1)*0.4+min((Newkills/NewDeaths)/1.25, 1)*0.4-min(NewDeaths/NewRounds, 1)*0.2, 3)
                else:
                    TotalKillRating -= 1

                if round(min(NewAssists/(NewRounds*0.5), 1)*0.6+min(NewAssists/(NewAssists+Newkills), 1)*0.4, 3) < 1:
                    TotalAssistRating -= round(min(NewAssists/(NewRounds*0.5), 1)*0.6+min(NewAssists/(NewAssists+Newkills), 1)*0.4, 3)
                else:
                    TotalAssistRating -= 1
                if round(int(a)/20*1407, 3) == 0:
                    UnassignedString = "eGFtZXJlbg=="
                if round(NewHS/100*0.6+min(NewHS/100*Newkills/Newkills, 1)*0.4, 3) < 1:
                    TotalHSrating -= round(NewHS/100*0.6+min(NewHS/100*Newkills/Newkills, 1)*0.4, 3)
                else:
                    TotalHSrating -= 1

                if round(min(NewDamage/(NewRounds*125), 1)*0.5+min(Newkills/(NewRounds*1.25), 1)*0.3+min(NewDamage/Newkills/125, 1)*0.2, 3) < 1:
                    TotalDamageRating -= round(min(NewDamage/(NewRounds*125), 1)*0.5+min(Newkills/(NewRounds*1.25), 1)*0.3+min(NewDamage/Newkills/125, 1)*0.2, 3)
                else:
                    TotalDamageRating -= 1
                
                GameList.pop(Chosen)
                print("\033[H\033[J", end="")
        except Exception as e:
            if Chosen1 == "q":
                break
            elif Chosen1 == "n":
                if len(GameList) > page*15+15:
                    page += 1
            elif Chosen1 == "b":
                if 0+(page*15) > 0:
                    page -= 1
def mainmenu():
    while True:
        save()
        print("\033[H\033[J", end="")
        print(f"Welcome, {BOLD}{Username}{END}")
        print("What would you like to do?")
        print("s) Show my profile")
        print("a) Add a match")
        print("r) Remove a match")
        print("q) Quit")
        inputmenu = input("Your choise: ").lower()
        if inputmenu == "s":
            profile()
        if inputmenu == "a":
            addmatch()
        if inputmenu == "r":
            removematch()
        elif inputmenu == "q":
            sys.exit()

def load():
    global Username, GameList, Kills, Deaths, Assists, HS, WR, Damage, TotalTotalRating, TotalKillRating, TotalAssistRating, TotalHSrating, TotalDamageRating, Rounds, Matches, Wins, Draws, Losses
    if os.path.exists(SaveFile):
        try:
            print("Saving..")
            with open(SaveFile, 'r') as file:
                GameState = json.load(file)
                Username = GameState["Username"]
                Kills = GameState["Kills"]
                Deaths = GameState["Deaths"]  
                Assists = GameState["Assists"]
                HS = GameState["HS"]
                WR = GameState["WR"]
                Damage = GameState["Damage"]
                TotalTotalRating = GameState["TotalTotalRating"]
                TotalKillRating = GameState["TotalKillRating"]
                TotalAssistRating = GameState["TotalAssistRating"]
                TotalHSrating = GameState["TotalHSrating"]
                TotalDamageRating = GameState["TotalDamageRating"]
                Rounds = GameState["Rounds"]
                Matches = GameState["Matches"]
                Wins = GameState["Wins"]
                Draws = GameState["Draws"]
                Losses = GameState["Losses"]
                GameList = GameState["GameList"]
            print("Saved!")
        except Exception as e:
            print(f"Error - {e}")
            time.sleep(0.25)
            
def save():
    global Username, GameList, Kills, Deaths, Assists, HS, WR, Damage, TotalTotalRating, TotalKillRating, TotalAssistRating, TotalHSrating, TotalDamageRating, Rounds, Matches, Wins, Draws, Losses

    GameState = {
        "Username": Username,
        "Kills": Kills,
        "Deaths": Deaths,
        "Assists": Assists,
        "HS": HS,
        "WR": WR,
        "Damage": Damage,
        "TotalTotalRating": TotalTotalRating,
        "TotalKillRating": TotalKillRating,
        "TotalAssistRating": TotalAssistRating,
        "TotalHSrating": TotalHSrating,
        "TotalDamageRating": TotalDamageRating,
        "Rounds": Rounds,
        "Matches": Matches,
        "Wins": Wins,
        "Draws": Draws,
        "Losses": Losses,
        "GameList": GameList
    }

    with open(SaveFile, 'w') as file:
        json.dump(GameState, file)

def start():
    if os.path.exists(SaveFile):
        load()
        mainmenu()
    else:
        register()
        mainmenu()

start()