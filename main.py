#int=číslo , float = desetinné číslo, string = text
#prtint("zpráva") -> print("Michal","Kučera")
#print("10","+","10","=",(10+10))

#Vytvoř (nadefinuj) dvě proměnné, jmeno a vek. Následně do nich přiřaď hodnotu. Nakonec obsah proměnných vypiš na obrazovku.
jmeno = "Václav Kotyk"
vek = 25
email = "vaclavkotyk@seznam.cz"
print("Jmenuji se", jmeno, "a je mi", vek, "let a kontakt na mě je", email)

#Vytvoř dvě číselné proměnné a pak jednu další, ve které bude součet hodnot z předchozích dvou proměnných. Výsledek vypiš na obrazovku.
cisilko1 = 10
cisilko2 = 8
soucet = cisilko1 + cisilko2
print(soucet)

#Vytvoř proměnné cislo1 a cislo2. Do konzole vypiš jejich součet, součin, rozdíl a podíl, ve formátu "1 + 1 = 2".
cislo1 = 24
cislo2 = 8
print(cislo1, "+", cislo2, "=", (cislo1+cislo2))
print(cislo1, "-", cislo2, "=", (cislo1-cislo2))
print(cislo1, "*", cislo2, "=", (cislo1*cislo2))
print(cislo1, "/", cislo2, "=", (cislo1/cislo2))

#Vytvoř proměnnou obsahující text tvého křestního jména (tak aby nezačínal a nekončil mezerou). Vytvoř druhou proměnnou obsahující text tvého příjmení (opět nesmí začínat ani končit mezerou). Nakonec vytvoř proměnnou, ve které bude "spojení" těchto dvou proměnných s tím, že je spojíš mezerou. Výsledný text vypiš na obrazovku.
jmeno = "Václav"
prijmeni = "Kotyk"
print(jmeno+" "+prijmeni)
print(jmeno+""+prijmeni)
print(jmeno,prijmeni)

#Knihovna random
#from random import randint
#nahodneCisloTohotoProgramu = randint(1, 10)
#print(nahodneCisloTohotoProgramu)

#Vstup od uživatele
#input("Zadej své jméno")
#jmeno = input ("Zadej své jméno")
#print (jmeno)

#Změna datového typu = parsování - takto by hodilo chybu, proto nutné převést na int - viz dále
#cislo = input("Zadej cislo")
#print(cislo + 1)

#cislo = int(input("Zadej cislo"))
#print(cislo + 1)

#Vytvoř proměnnou uspesnost, do které vložíš číslo z generátoru náhodných čísel, a uprav ho tak, aby hodnota mohla být od 0 do 100. Hodnotu této proměnné vypiš.
from random import randint

uspesnost = randint(1, 100)
print(uspesnost)

#Vytvoř program, který načte číslo od uživatele, vynásobí ho dvěma a zase ho vypíše.
cislo = int(input("Zadej číslo a řeknu ti jeho dvojnásobek "))
print(cislo * 2)

cislo = int(input("Zadej číslo "))
print("Tvoje číslo * 2 se rovná:", cislo * 2)

#Vytvoř program, který vypíše text podle vzoru "Hozeno na kostce: 5", s tím, že hozené číslo se bude generovat náhodně, v intervalu 1 až 6.
from random import randint

print("Hozeno na kostce: ", randint(1, 6))

#Vytvoř proměnnou a přiřaď do ní číslo s desetinným rozvojem. Dále vytvoř druhou proměnnou a zaokrouhli do ní původní desetinné číslo. Obě hodnoty vypiš na obrazovku. (Hledej na Google!)
cislo_bez_zaokrouhleni = 2.5
cislo_zaokrouhlene = round(cislo_bez_zaokrouhleni)

print("Tvé původní číslo bylo", cislo_bez_zaokrouhleni, "a po zaokrouhlení dostaneš", cislo_zaokrouhlene)


#(Bonus) Vytvoř jednoduchý program na sčítání. Požádej uživatele o první číslo výpisem jako je např. "Zadej prvni cislo:", hodnotu ulož do proměnné. b. Podobně načti druhé číslo. c. Vypiš uživateli výsledek ve formátu "5 + 8 = 40".
cislo3 = int(input("Zadej první číslo: "))

cislo4 = int(input("Zadej druhé číslo: "))

vysledek = cislo3 + cislo4
print("Součet tvého prvního a druhého čísla je: ", cislo3, "+", cislo4, "=", vysledek)

#Podmínky
#if výraz: 
  #příkaz (pravdivá větev, minimálně tato musít být, pokud nikdy nenabyde negativního stavu nikdy, tak stačí pravdivá větev)
  #příkaz
#else:
  #příkaz (pokud je nepravdivý)
  #příkaz

vek = int(input("Vítejte na e-shopu s alkoholem. Pro přístup na web, zadejte svůj věk: "))

if vek >= 18:
  print("Vítejte, vyberte si z naší široké nabídky v levém menu.")
else:
  print("Litujeme. Přístup na web je umožněn pouze dospělým osobám.")


#tohle ještě nefunguje, musím odladit

#vek = 20
#kraj = praha

#if vek >= 18:
  #print("Vítejte na e-shopu s alkoholem")
  #if kraj == "morava":
      #print("daj si slivovicu")
  #else:
      #print("dej si prosecco")
#else:
  #print("Litujeme. Přístup na web je umožněn pouze dospělým osobám.")

#Elif ukázka
#if cislo > 100:
  #print("cislo je vetsi nez 100") 
#elif cislo < 0:
  #print("cislo je nezaporne") 
#else:
  #print("je mezi") 

#Vytvoř proměnnou, do které vložíš výsledek z generátoru náhodných čísel. Vypiš hodnotu této proměnné. Pokud její hodnota bude větší než 0.5, vypiš text "Cislo je vetsi nez 0.5".
from random import random

nahodne_cislo = random()
print ("Vygenerované číslo je: ", nahodne_cislo)
if nahodne_cislo > 0.5:
  print("Toto vygenerované číslo je větší než 0.5")
else:
  print("Toto vygenerované číslo je menší než 0.5")

#Vytvoř proměnnou, do které načteš číslo od uživatele z klávesnice. Pokud je hodnota této proměnné větší než 100, vypiš "Cislo je vetsi nez 100". A pokud je hodnota této proměnné menší než nula, vypiš "Cislo je zaporne".
cislo_od_uzivatele = int(input("Zadejte libovolné číslo: "))

if cislo_od_uzivatele > 100:
  print("Toto zadané číslo je větší než 100.")
elif cislo_od_uzivatele < 0:
   print("Toto zadané číslo je záporné.")
else:
  print("Toto zadané číslo je v rozsahu 0-100.")


#Vytvoř 2 proměnné. Do jedné ulož nějaké heslo (jako text) a do druhé vstup od uživatele. Pokud se hodnota zadaná uživatelem bude rovnat heslu v proměnné, tak vypiš "přihlášen", v opačném případě "přístup zamítnut".

spravne_heslo = "heslo123"
zadane_heslo = input("Zadejte heslo: ")

if zadane_heslo == spravne_heslo:
  print("Jste přihlášeni!")
else:
  print ("Přístup zamítnut.")

#Vytvoř proměnnou, do které uložíš číslo zadané uživatelem. Pomocí podmínky zjisti, jestli je číslo liché nebo sudé. (využij zbytek po dělení - %)

cislo_zadane = int(input("Zadejte libovolné číslo pro ověření, zda je sudé nebo liché: "))

if  (cislo_zadane % 2) == 0:
  print("Toto zadané číslo je sudé.")
else:
   print("Toto zadané číslo je liché.")


#(BONUS) Vytvoř 3 proměnné, do kterých načteš čísla od uživatele z klávesnice. Vytvoř další proměnnou, do které uložíš aritmetický průměr tří předchozích proměnných. Tento průměr zaokrouhli a vypiš uživateli slovním hodnocením, jakou známku dostal. (1 – výborný, 2 – chvalitebný, 3 – dobrý, 4 – dostatečný, 5 – nedostatečný).