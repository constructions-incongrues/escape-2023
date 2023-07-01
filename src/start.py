import os
import sys
import codecs
import time
from matrix3 import matrix
import termdown
from tqdm import tqdm

#UTF8Writer = codecs.getwriter('utf8')
#sys.stdout = UTF8Writer(sys.stdout)
#print(u'e with obfuscation: é')
#print(u'⢰⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣠⣿⣿⠐⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
#print(u'⢰⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣠⣿⣿⠐⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
#time.sleep(3)
os.system('clear')
prenom = ''
erreur = 0

step = 1
finish = False

print("")
print("                                _                 ")
print("  ___ _ __   __ _  ___ ___  ___| |__ (_)_ __  ___ ")
print(" / __| '_ \ / _` |/ __/ _ \/ __| '_ \| | '_ \/ __|")
print(" \__ \ |_| | |_| | |_|  __/\__ \ | | | | |_| \__ \ ")
print(" |___/ .__/ \__,_|\___\___||___/_| |_|_| .__/|___/")
print("     |_|                               |_|        ")

input()

while finish == False:

    if step == 1:
#        if choice := 'to':
        os.system('clear')
#            print("\nTon prénom n'est pas un prénom\n")
        prenom = input("Bonjour, quel est ton prénom ?\n")
        if prenom.lower() == 'jimmy':
            step = 2
    elif step == 2:
        os.system('clear')
        aventure = input("Salut " + prenom + ", es-tu prêt à te lancer dans l’aventure ?\nOui - Non\n")
        if aventure.lower() == 'oui':
            step = 3
        else:
            step = 1
    elif step == 3:
        os.system('clear')
        mdp = input("Quel est le mot de passe ? :\n")
        if mdp.lower() == 'james':
            step = 4
            os.system('clear')
            print("Tu incarnes « Le Mercenaire ».\n")
            print(u'⢰⣶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣠⣿⣿⠐⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
            print("⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣿⣿⣟⣹⣇⣀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀.")
            print("⠀⠀⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⣀⠤⠂⠀⠀⣴⡷⣿⣿⣿⣿⣿⣧⡷⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁")
            print("⠀⠀⠀⠀⠀⢿⢿⡀⠀⠀⢀⠴⠋⠀⠀⠀⠀⠸⣇⣇⢿⣾⣿⣿⠻⣇⣵⣦⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣆⣀⣠⣴⡆")
            print("⠀⠀⠀⠀⠀⢸⣿⣿⡤⠚⠁⠀⠀⠀⠀⠀⠀⠀⢿⡿⣯⣿⣿⣿⠜⣿⠿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠟⠉⠀")
            print("⠀⠀⠀⠀⠀⠸⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⢿⠃⠈⣾⣿⣿⡼⠁⡄⢹⡁⠀⠀⠀⠀⠀⠀⠀⣰⣿⡿⠋⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⣠⣾⣝⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠈⠀⢠⣸⣿⣿⣧⣴⡶⢶⣶⣶⣤⣤⣤⣄⣀⣾⣷⠏⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⣼⣿⣾⣾⣿⣿⠆⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⡿⢿⣿⣿⣿⣿⠿⣿⡟⡼⠁⠀⠉⠻⣯⣥⡀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠘⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⣠⣾⢿⣿⢿⣿⣾⣿⡿⠟⠁⠀⢠⣿⢁⣿⣶⣄⠀⠀⠈⢿⡵⡄⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⢸⣿⢧⣤⡄⠀⠀⠀⠀⢀⣴⢋⣼⡿⢡⣾⣿⡟⠋⠀⠀⠀⠀⣼⣿⣾⣯⠻⣿⣧⡄⠀⠘⣷⢱⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⢿⣧⣷⡹⣦⠀⠀⢀⣾⠇⣾⠿⣷⣿⡿⠋⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣾⣼⢿⣿⣷⣆⣿⡎⡄⠀⠀⠀⠀")
        else:
            print("")
            print("                      :::!~!!!!!:.")
            print("                  .xUHWH!! !!?M88WHX:.")
            print("                .X*#M@$!!  !X!M$$$$$$WWx:.")
            print("               :!!!!!!?H! :!$!$$$$$$$$$$8X:")
            print("              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:")
            print("             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!")
            print("             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!")
            print("               !:~~~ .:!M'T#$$$$WX??#MRRMMM!")
            print("               ~?WuxiW*`   `'#$$$$8!!!!??!!!")
            print("             :X- M$$$$       `'T#$T~!8$WUXU~")
            print("            :%`  ~#$$$m:        ~!~ ?$$$$$$")
            print("          :!`.-   ~T$$$$8xx.  .xWW- ~''##*'")
            print(".....   -~~:<` !    ~?T#$$@@W@*?$$      /`")
            print("W$@@M!!! .!~~ !!     .:XUW$W!~ `'~:    :")
            print("#'~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`")
            print(":::~:!!`:X~ .: ?H.!u '$$$B$$$!W:U!T$$M~")
            print(".~~   :X@!.-~   ?@WTWo('*$$$W$TH$! `")
            print("Wi.~!X$?!-~    : ?$$$B$Wu('**$RM!")
            print("$R@i.~~ !     :   ~$$$$$B$$en:``")
            print("?MXT@Wx.~    :     ~'##*$$$$M~")
            time.sleep(4)
            step = 1
    elif step == 4:
        print("")
        print("Qu’est-ce qui te fais de l’ombre ?\n1. Cyrus\n2. Kepler-69C\n3. Vandervecken\n4. Proxima Centauri b\n5. Terre\n")
        print("")
        print("                     `. ___")
        print("                    __,' __`.                _..----....____")
        print("        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'")
        print("  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'")
        print(",'________________                          \`-._`-','")
        print(" `._  JOLU GAME   ```````````------...___   '-.._'-:")
        print("    ```--.._      ,.                     ````--...__\-.")
        print("            `.--. `-`                       ____    |  |`")
        print("              `. `.                       ,'`````.  ;  ;`")
        print("                `._`.        __________   `.      \ '__/`")
        print("                   `-:._____/______/___/____`.     \  `")
        print("                               |       `._    `.    \ ")
        print("                               `._________`-.   `.   `.___")
        print("                                                   `------'`")
        ombre = input("")
        if ombre == "3":
            step = 5
        else:
            erreur = erreur + 1
            if erreur == 1:
                os.system('clear')
                os.system('termdown 120')
#                for x in range(0, 3):
#                    os.system('clear')
#                    print(3 - x)
#                    time.sleep(1)                
#                time.sleep(3)
            #elif erreur == 2:
            #    os.system('termdown 6')
#           #     for x in range(0, 6):
#           #         os.system('clear')
#           #         print(6 - x)
#           #         time.sleep(1)                
            elif erreur == 2:
                os.system('clear')
                print("            	⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁")
                print("⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀")
                print("⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀")
                print("⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀")
                print("⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀")
                print("⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀")
                print("⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆")
                print("⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀")
                print("⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀")
                print("⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀")
                print("⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀")
                print("⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                #for x in range(0, 6):
                #    os.system('clear')
                #    print(6 - x)
                #    time.sleep(1)                
                input()
                erreur = 0
                step = 1
    elif step == 5:
        os.system('clear')
        combat = input("Qui devrez-vous affronter ?\n")
        if combat.lower() == "cyrus":
            step = 6
            #print("GLITCH")
            #time.sleep(1)                
            matrix(5)
    elif step == 6:
        os.system('clear')
        commande = input("L’horloge interne du système est déréglée. Saisir la commande de programmation :\n")
        if commande.lower() == 'sudo date reset':
#        if commande == 'sudo date --set="1999-12-31 10:05:59"'
            step = 7
    elif step == 7:
        os.system('clear')
        print("Réinitialisation …\n")
        time.sleep(2)
        for i in tqdm(range(120)):
            time.sleep(1)
#        for x in range(0, 5):
#            os.system('clear')
#            print(5 - x)
#            time.sleep(1)
        os.system('clear')
        print("Félicitation ! L’horloge est de nouveau synchronisée.\n")
        
        print("")
        print("              _-o#&&*''''?d:>b\_")
        print("          _o/'`''  '',, dMMMMHo_")
        print("       .o&#'        `'MbHMMMMMMMMMMMHo.")
        print("     .o'' '         vodM*$&&HMMMMMMMMMM?.")
        print("    ,'              $M&ood,~'`(&##MMMMMMH")
        print("   /               ,MMMMMMM#b?#bob1984HMMML")
        print("  &              ?MMMMMMMMMMMMMMMMMMMMM$R*Hk")
        print(" ?$.            :MMM1984MMMMMMMMMMMM/HMMM|`*L")
        print("|               |MMMMMMMMMMMMMMMMMMMMbMH'   T,")
        print("$H#:            `*MMMMMMMMMM1984MMMMMMb#}'  `?")
        print("]MMH#             ''*''''*#MMMMMMMMMMMMM'    -")
        print("MMMMMb_                   |MMMMMMMMMMMP'     :")
        print("HMMMMMMMHo                 `MMMMMMMMMT       .")
        print("?MMMMMMMMP                  MM1984MMM}       -")
        print("-?MMMMMMM                  |MMMMMMMMM?,d-    '")
        print(" :|MMMMMM-                 `MMMMMMMT .M|.   :")
        print("  .MMMM[                    &MJOLU*' `'    .")
        print("   :MMMk                    `MMM#'        -")
        print("     &M}                     `          .-")
        print("      `&.                             .")
        print("        `~,   .                     ./")
        print("            . _                  .-")
        print("              '`--._,dd###pp=""'")
        time.sleep(4000)
#        finish = True

        
