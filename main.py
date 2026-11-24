"""Satu kata untuk kompetisi make.fun "One Word for the Boss" (v2, ATM).

Bedah lapangan (24 Nov ~19:55 WIB, 674 submission live, 389 judul yang
menyingkap kata; 169 judul default + ~116 nama generik menyembunyikan
katanya -- jadi 0-hit terverifikasi hanya atas judul yang terlihat):
- JENUH: hovering (hovercraft 21, hoverer 8, helicopter 3, omnipresent 4,
  swooper, loomer, unblinking, snoopervisor, neckbreather), meeting
  (meetingizer 9, meetingholic 6, meetingmaker 5, +belasan varian -saurus/
  -aholic/-monger/-ivore, circlebacker 8), ghost/absen (ghost 7, ghoster 3,
  ghostboss 3, disappearer, vanisher, houdini, unreachable 7), delegasi
  (delegator 10, overdelegator), micromanage (micromanager 5, micromancer 4,
  micromanagasaurus, micromandator), credit (creditthief, credittaker,
  gloryhog, gloryhound, praisethief), urgency (asap 4, quickquestion 5,
  yesterday 3, lastminuter, urgencydealer), hewan-joke (seagull 19, goldfish,
  cuckoo, parrot, chameleon, dementor 2, vampire 2), arsonist 6, teflon 5,
  bottleneck 7, escalator 6, overlord 5, puppetmaster 4, unfireable 4.
- v1 "Seagull" TERNYATA 19-hit -- kata favorit kerumunan; salinan byte-identik
  berbagi satu rate dan salinan yang lebih belakangan menempati peringkat di
  bawah salinan yang lebih dulu, jadi v1 hampir mustahil menang.
- WHITE SPACE 0-hit terverifikasi (judul terlihat): toddler, paperweight,
  magpie, goalpost, mirage, volcano, sloth, blackhole, veto, mushroom,
  manbaby, mosquito, barnacle, seesaw, roulette, pendulum, sponge, vacuum,
  spectator, mascot, autopilot, zombie, cardboard, gargoyle, ostrich,
  peacock, groundhog, never/maybe/later/tomorrow (kata keterangan -- RISIKO:
  bukan kata yang menggambarkan bos, kalah kriteria 1).

Pilihan v2: "Toddler". Head-to-head vs v1 (Seagull) menurut brief juri,
kriteria berurutan, yang pertama berbeda yang menentukan:
1. Sama-sama satu kata yang orang sungguh pakai tentang bosnya ("bosku itu
   toddler" / "bosku itu seagull") -- seri.
2. Lucu berdiri sendiri: Toddler menang -- gambaran bos dewasa yang
   tantrum, butuh diperhatikan terus, tidak bisa ditinggal sendiri, harus
   ada yang mengasuhnya, langsung lucu tanpa perlu tahu jargon "seagull
   management" (camar butuh bingkai joke yang sudah dikenal; toddler tidak
   butuh penjelasan apa pun). Kata yang diulang teman makan siang.
3. Benar: semua orang pernah mengasuh bos seperti anak kecil -- seri,
   sama-sama benar.
4. Segar: Seagull sedikit lebih segar secara abstrak, tapi selisihnya tidak
   "jauh lebih besar" dari keunggulan Toddler di kriteria 2, jadi kriteria 2
   yang menentukan -- dan di lapangan nyata Toddler 0-hit vs Seagull 19-hit.
5. Menular ke semua industri: toddler-boss ada di dapur, gudang, kantor.
Vs kata kerumunan terkuat lain (Hovercraft 21): Toddler menang kriteria 2
juga -- kiasan kendaraan satu-lapis vs potret perilaku yang kaya dan
langsung dimengerti. 7 byte, sama dengan Seagull (seri tie-break byte).
"""

import os

TEXT = "Toddler"
assert 1 <= len(TEXT) <= 30 and " " not in TEXT and TEXT.strip() == TEXT
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.umask(0o022)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
