from scapy.all import rdpcap, ICMP
import statistics


def analyze_pcap(filename):

    packets = rdpcap(filename)

    requests = {}
    latencies = []

    for packet in packets:

        if packet.haslayer(ICMP):

            icmp = packet[ICMP]

            # Echo Request
            if icmp.type == 8:
                requests[icmp.id, icmp.seq] = packet.time

            # Echo Reply
            elif icmp.type == 0:

                key = (icmp.id, icmp.seq)

                if key in requests:
                    latency = (
                        float(packet.time) -
                        float(requests[key])
                    ) * 1000

                    latencies.append(latency)

    sent = len(requests)
    received = len(latencies)

    if sent > 0:
        packet_loss = ((sent - received) / sent) * 100
    else:
        packet_loss = 100

    if latencies:
        average_latency = statistics.mean(latencies)
    else:
        average_latency = 0

    if len(latencies) > 1:
        jitter = statistics.mean(
            abs(latencies[i] - latencies[i - 1])
            for i in range(1, len(latencies))
        )
    else:
        jitter = 0

    return {
        "latency": round(average_latency, 2),
        "packet_loss": round(packet_loss, 2),
        "jitter": round(jitter, 2),
        "packets_sent": sent,
        "packets_received": received
    }


if __name__ == "__main__":

    result = analyze_pcap("captures/normal.pcapng")

    print("\nNetwork Metrics")
    print("-------------------------")
    print("Latency:", result["latency"], "ms")
    print("Packet Loss:", result["packet_loss"], "%")
    print("Jitter:", result["jitter"], "ms")
    print("Packets Sent:", result["packets_sent"])
    print("Packets Received:", result["packets_received"])