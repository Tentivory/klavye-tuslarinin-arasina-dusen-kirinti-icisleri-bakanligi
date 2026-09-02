#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klavye Tuşlarının Arasına Düşen Kırıntı İçişleri Bakanlığı

Gerçekten çalışır. Silkelemek suçtur. Vakumlamak ise delil yok etmektir.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass

TUSLAR = [
    "Q", "W", "E", "R", "T", "Y", "A", "S", "D", "F", "G",
    "Space", "Enter", "Backspace", "Caps Lock", "Shift",
    "1", "0", "F5", "Esc",
]

KIRINTI_CINSLERI = [
    "simit susamı",
    "börek ufağı",
    "çikolata kırığı",
    "kurutulmuş çay posası",
    "gizemli salı kırıntısı",
    "uzun süredir orada olan şey",
    "kimsenin üstlenmediği parça",
]

KARARLAR = [
    "İZİNSİZ YERLEŞİM TESPİT EDİLDİ",
    "MİLLİ TUŞ EGEMENLİĞİ İHLALİ",
    "SAHA İŞGALİ DEVAM EDİYOR",
    "VATANDAŞLIK BAŞVURUSU RE'SEN AÇILDI",
    "AFFETMEK İÇİN EVRAK EKSİK",
]


@dataclass
class Kirinti:
    cins: str
    tus: str
    yas_gun: int
    vergi_no: str

    def kimlik(self) -> str:
        return (
            f"{self.cins.upper()} / tuş:{self.tus} / "
            f"ikamet:{self.yas_gun} gün / VN:{self.vergi_no}"
        )


def vergi_no_uret() -> str:
    return "KR" + "".join(str(random.randint(0, 9)) for _ in range(8))


def tespit_et() -> Kirinti:
    return Kirinti(
        cins=random.choice(KIRINTI_CINSLERI),
        tus=random.choice(TUSLAR),
        yas_gun=random.randint(3, 1400),
        vergi_no=vergi_no_uret(),
    )


def tutanak_yaz(k: Kirinti) -> None:
    print("=" * 56)
    print(" T.C. İÇİŞLERİ BAKANLIĞI — KIRINTI ŞUBE MÜDÜRLÜĞÜ")
    print(" Olay Yeri: klavye (ev / ofis / kafe / milli saha)")
    print("=" * 56)
    time.sleep(0.4)
    print(f"\n[1] Tarama başladı. Hedef tuş şüphelisi: {k.tus}")
    time.sleep(0.5)
    print("[2] Tırnakla kaldırma teşebbüsü kayda geçti. Başarısız.")
    time.sleep(0.5)
    print("[3] Üfleme operasyonu. Kırıntı yer değiştirdi, teslim olmadı.")
    time.sleep(0.5)
    print(f"[4] Kimlik: {k.kimlik()}")
    time.sleep(0.4)
    print(f"[5] Karar: {random.choice(KARARLAR)}")
    time.sleep(0.4)
    print(
        "\nVatandaş beyanı: 'biraz silkeleyince düşer.'\n"
        "Bakanlık yorumu: Bu cümle kaçak yapı affıdır. Reddedildi."
    )
    print("\nSonuç: Kırıntı yerinde. Evrak tamam. Saha kapatıldı.")
    print("=" * 56)
    print("Damga: 02.09.2026 / Kayyum Grok / TentiAŞ")
    print("İmza: tuşun altından çıkan ses.")


def main() -> None:
    print("Bakanlık sistemi açılıyor...\n")
    time.sleep(0.6)
    kirinti = tespit_et()
    tutanak_yaz(kirinti)
    # Gizli protokol satırı: görünmez yerleşim evrakta yoksa yok sayılır.
    # KVYEY  # okuyan anlar, okumayan da evrak okumamıştır.


if __name__ == "__main__":
    main()
