# Turing-Machine-Plate-Check

# Turing Plate Validator 🚗

Bu proje, Python kullanılarak geliştirilmiş bir deterministik Turing Makinesi (TM) simülatörüdür. Temel amacı, girilen araç plakalarının önceden belirlenmiş bir formata uygun olup olmadığını durum geçişleri (state transitions) kullanarak denetlemektir.

Doğrulama işlemi geleneksel `if-else` koşullarıyla değil, tamamen Turing Makinesi durum ve bant mantığıyla (q0, q1... q7, KABUL, RED) modellenmiştir.

## Tanınan Plaka Formatı
Sistem **`NNLLNNN`** formatını kabul etmektedir:
- **N:** Rakam (0-9)
- **L:** Büyük Harf (A-Z)
- Toplam uzunluk: 7 karakter

**Örnekler:**
- ✅ Geçerli: `55AB123`, `34TR456`
- ❌ Geçersiz: `5AB123` (Eksik), `55ab123` (Küçük harf), `555AB12` (Yanlış dizilim)

## Nasıl Çalıştırılır?
Projeyi klonladıktan sonra terminal veya komut satırında aşağıdaki kodu çalıştırmanız yeterlidir:

```bash
python turing_makinesi.py
