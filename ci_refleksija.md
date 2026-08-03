# Refleksija par CI, testēšanu un procesiem

1. **Kas notika, kad tests bija kļūdains?**
   - Kad testā tika ievadīta nepareiza vērtība un kods tika nosūtīts uz GitHub, GitHub Actions automātiski konstatēja kļūdu un CI statuss kļuva sarkans (*failing*), norādot uz testa izgāšanos.

2. **Kāpēc CI palīdz ātri pamanīt kļūdas?**
   - CI (Continuous Integration) automātiski palaiž visus testus uzreiz pēc katra `push` notikuma mākoņvidē. Tas ļauj atklāt kļūdas uzreiz to rašanās brīdī, nevis vēlāk programmas izstrādes vai lietošanas laikā.

3. **Kā DoD palīdz komandai?**
   - Definition of Done (DoD) ievieš skaidrus un vienotus kritērijus visai komandai, nosakot, kad darbs ir tiešām pabeigts. Tas samazina kļūdu skaitu un uzlabo koda kvalitāti, jo nekas netiek palaists bez testu un CI apstiprinājuma.

4. **Kā mainījās tava attieksme pret git push?**
   - Attieksme kļuva apzinātāka un atbildīgāka. Ja agrāk `git push` bija tikai datu sinhronizācija, tad tagad tas ir nopietns kontroles punkts, jo katrs `push` iedarbina automātiskās pārbaudes, un kļūdas gadījumā parādīsies sarkans statuss.