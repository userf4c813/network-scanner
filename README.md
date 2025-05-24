
# 🔎 Python Network Scanner
---

 Layihənin Məqsədi

- IP aralığını təyin edib hostları tapmaq
- TCP port scanning
- Açıq portlardan banner məlumatı toplamaq
- Paralel scanning (threading ilə performans)
- JSON və konsol nəticələri
- Komanda işi və versiya nəzarəti təcrübəsi qazanmaq

---

 Layihə Strukturu

```bash
network-scanner/
├── scanner/
│   ├── ip_generator.py
│   ├── port_scanner.py
│   ├── threading_worker.py
│   └── banner_grabber.py
├── reporter/
│   └── report_generator.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
