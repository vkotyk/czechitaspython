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
cislo = 2.5
cislo_zaokrouhlene = round(cislo)

print("Tvé původní číslo bylo", cislo, "a po zaokrouhlení dostaneš", cislo_zaokrouhlene)


#(Bonus) Vytvoř jednoduchý program na sčítání. Požádej uživatele o první číslo výpisem jako je např. "Zadej prvni cislo:", hodnotu ulož do proměnné. b. Podobně načti druhé číslo. c. Vypiš uživateli výsledek ve formátu "5 + 8 = 40".
cislo1 = int(input("Zadej první číslo: "))

cislo2 = int(input("Zadej druhé číslo: "))

vysledek = cislo1 + cislo2
print("Součet tvého prvního a druhého čísla je: ", cislo1, "+", cislo2, "=", vysledek)

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


#vek = 20
#kraj = praha

#tohle ještě nefunguje, musím odladit
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