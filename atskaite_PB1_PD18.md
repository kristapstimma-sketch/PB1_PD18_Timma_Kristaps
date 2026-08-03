
# Praktiskā darba atskaite

---

## 1. Vispārīgā informācija

- Vārds, Uzvārds: Kristaps Timma        
- Grupa: PIN 77151      
- Praktiskā darba kods: PB1_PD18        
- Datums: 2026.08.04.               

---

## 2. Darba mērķis

Praktiskā darba mērķis bija apgūt programmatūras testēšanas un versiju vadības pamatus, izmantojot Python unit testus, Git un GitHub Actions automatizāciju. Tika attīstītas prasmes konfigurēt nepārtrauktas integrācijas (CI) procesus, analizēt testu statusus un pārvaldīt izstrādes ciklu.     
---

## 3. Izmantotā vide un rīki

- Operētājsistēma:      
Windows 11
- Programmas / rīki:        
Git, GitHub, koda redaktors (VS Code)       
- Versijas (ja nepieciešams):       
Python 3.14, Git
- Papildu bibliotēkas / servisi (ja attiecas):      
GitHub Actions (CI/CD), Python unittest (iebūvētā bibliotēka testēšanai), GitHub Projects (Kanban dēlis uzdevumu pārvaldībai)

---

## 4. Uzdevumu izpilde

---

### Uzdevums 1

- Ko darīju:        
Izveidoju jaunu GitHub repozitoriju projektam, definēju četrus nepieciešamos uzdevumus (Issues) un iestatīju Kanban dēli uzdevumu plānošanai un pārvaldībai.        
- Izmantotās komandas / darbības:       
GitHub platformā izveidoju jaunu publisku/privātu repozitoriju ar nosaukumu PB1_PD18_Uzvards_Vards.     
Sadaļā Issues izveidoju četrus uzdevumus        .
Sadaļā Projects izveidoju Kanban dēli ar trim kolonnām: To Do, Doing un Done, un ievietoju tajā izveidotos uzdevumus.       
- Rezultāts:        
Izveidots un strukturēts GitHub repozitorijs ar aktīvu uzdevumu sarakstu un Kanban dēli, kas nodrošina vizuālu darba gaitu un gatavību turpmākajai programmatūras izstrādei.        


---

### Uzdevums 2

- Ko darīju:        
Izveidoju failu kalkulators.py un realizēju pamata funkciju divu skaitļu saskaitīšanai.     
- Izmantotās komandas / darbības:       
Izveidoju jaunu failu kalkulators.py.       
Uzrakstīju funkciju.        
Kanban dēlī pārvietoju uzdevumu "Izveidot funkciju" no Doing uz Done.       
- Rezultāts:        
Rezultāts: Fails ir izveidots un saglabāts projekta saknes mapē, un funkcija korekti veic skaitļu saskaitīšanu bez kļūdām.      

---

### Uzdevums 3

- Ko darīju:        
Izveidoju vienību testa failu test_kalkulators.py, lai pārbaudītu funkcijas saskaitit darbību ar dažādiem argumentiem, izmantojot iebūvēto unittest bibliotēku.     
- Izmantotās komandas / darbības:       
Projekta direktorijā izveidoju jaunu failu test_kalkulators.py.     
Uzrakstīju testa klasi TestKalkulators, kas manto no unittest.TestCase, un pievienoju testu gadījumus pozitīviem, negatīviem skaitļiem un nullei.       
Lokāli palaidu testu terminālī ar komandu: python -m unittest test_kalkulators.py.       
Kanban dēlī pārvietoju uzdevumu "Uzrakstīt testu" no Doing uz Done.
- Rezultāts:        
Tests lokāli izpildās veiksmīgi un bez kļūdām (OK statuss terminālī), apstiprinot funkcijas pareizu darbību.        

---

### Uzdevums 4

- Ko darīju:        
Izveidoju GitHub Actions CI konfigurāciju automatizētai testēšanai, inicializēju Git repozitoriju lokālajā datorā, savienoju to ar GitHub un veiksmīgi augšupielādēju visus projekta failus.            
- Izmantotās komandas / darbības:       
Izveidoju failu .github/workflows/main.yml ar Python vidi un unittest palaišanas komandu.       
git init        
git add .       
git commit -m "Pievienoti visi projekta faili un CI"        
git remote set-url origin https://github.com/kristapstimma-sketch/PB1_PD18_Timma_Kristaps.git       
git pull origin main --allow-unrelated-histories        
git push -u origin main     
- Rezultāts:       
Projekta faili un CI konfigurācija ir pilnībā sinhronizēti ar GitHub, un GitHub Actions sadaļā CI izpildes statuss ir veiksmīgi zaļš (Success).     

---

### Uzdevums 5

- Ko darīju:        
Veicu CI eksperimentu, apzināti sabojājot vienu no testiem, lai pārbaudītu GitHub Actions reakciju uz kļūdām, un pēc tam salaboju testu atpakaļ, lai atjaunotu veiksmīgu izpildi.       
- Izmantotās komandas / darbības:       
Failā test_kalkulators.py apzināti nomainīju pareizo vērtību 5 uz nepareizo 6 (self.assertEqual(saskaitit(2, 3), 6)).       
GitHub sadaļā Actions pārliecinājos, ka CI statuss kļuva sarkans (failing).     
Atgriezu failā pareizo vērtību (5) un nosūtīju labojumu .    
- Rezultāts:        
Eksperiments izdevās – kļūdas gadījumā GitHub Actions uzrādīja kļūdu (sarkans statuss), bet pēc koda kļūdu novēršanas un atkārtotas augšupielādes CI statuss atkal kļuva veiksmīgi zaļš (passing), pierādot automatizētās testēšanas efektivitāti.

---

### Uzdevums 6

- Ko darīju:        
Papildināju repozitorija README.md failu ar Definition of Done (DoD) kritērijiem un izveidoju refleksijas failu ci_refleksija.md ar argumentētām atbildēm par CI, testēšanu un darba procesiem.     
- Izmantotās komandas / darbības:       
Atjaunināju README.md, iekļaujot prasīto DoD sarakstu.      
Izveidoju failu ci_refleksija.md ar četrām atbildēm uz refleksijas jautājumiem.     
Terminālī reģistrēju un nosūtīju failus uz GitHub.       
- Rezultāts:        
Visi projekta dokumentācijas un refleksijas uzdevumi ir veiksmīgi izpildīti, faili atrodas repozitorijā, un praktiskais darbs ir pilnībā pabeigts.      

---
      
## 5. Problēmas un to risinājumi

- Problēmas apraksts:       
Mēģinot pirmo reizi nosūtīt kodu uz GitHub, terminālī saņēmu kļūdu, jo lokālā mape vēl nebija inicializēta kā Git repozitorijs un nebija savienota ar attālināto repozitoriju.      
- Kļūdas ziņojums (ja bija):        
fatal: not a git repository (or any of the parent directories): .git un vēlāk remote: Repository not found.     
- Risinājums:       
git init, lai inicializēti mapi, precīzi nomainīju attālināto adresi uz savu GitHub repozitorija saiti un izmantoju git pull origin main --allow-unrelated-histories, lai veiksmīgi apvienotu failus.       
- Ko no tā iemācījos:       
Iemācījos pareizi strukturēt un sinhronizēt lokālo Git repozitoriju ar GitHub, kā arī risināt nesakritības starp lokālajiem un attālinātajiem failiem.      

---

## 6. Secinājumi

- Ko jaunu iemācījos šajā darbā?        
Iemācījos konfigurēt GitHub Actions CI automatizētai testēšanai, rakstīt un izpildīt unit testus ar Python unittest, kā arī pārvaldīt Git repozitorija sinhronizāciju un analizēt CI sarkanos un zaļos statusus.        
- Kas bija grūtākais?       
Sākotnējā Git repozitorija iestatīšana un sinhronizēšana ar GitHub, kad lokālie faili un attālinātais README.md sākotnēji atšķīrās.     
- Kas izdevās vislabāk?     
Veiksmīgi realizēt CI eksperimentu, pārliecinoties, ka GitHub Actions precīzi reaģē gan uz kļūdām (sarkans statuss), gan uz labojumiem (zaļš statuss).            

---

## 7. Pašvērtējums

Kopā punkti: 100 / 100

Pamatojums :       
Visi praktiskā darba uzdevumi ir pilnībā izpildīti: izveidots funkcionāls kalkulators un unit testi, veiksmīgi konfigurēts GitHub Actions CI, izpildīts CI eksperiments (pārbaudīts gan sarkanais kļūdas, gan zaļais veiksmīga testa statuss), kā arī izstrādāta visa prasītā dokumentācija, tajā skaitā Definition of Done (DoD) un refleksija. Visi koda un CI procesi strādā bez kļūdām.     

---

## 8. Pielikumi

- Pielikums 1 - test_kalkulators.py
- Pielikums 2 - kalkulators.py
- Pielikums 3 - ci_refleksija.md
- Pielikums 4 - README.md
- Pielikums 5 - .gitignore
- Pielikums 6 - .github/workflows/main.yml
