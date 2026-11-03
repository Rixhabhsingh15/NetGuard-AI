from pcap_analyzer import analyze_pcap

metrics = analyze_pcap("captures/normal.pcapng")

print(metrics)