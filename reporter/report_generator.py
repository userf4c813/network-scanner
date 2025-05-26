# report_generator.py
import datetime

def generate_report(scan_results, filename="scan_report.txt"):
    with open(filename, "w") as f:
        f.write("Scan Report\n")
        f.write(f"Date: {datetime.datetime.now()}\n\n")
        for result in scan_results:
            f.write(f"IP: {result.get('ip')}\n")
            f.write(f"Open Ports: {', '.join(map(str, result.get('ports', [])))}\n")
            f.write(f"Banner: {result.get('banner', 'N/A')}\n")
            f.write("-" * 40 + "\n")
    print(f"[+] Report saved to {filename}")
