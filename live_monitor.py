
import socket
import time
import re
import statistics

# GNS3 VPCS PC1 console connection
HOST = "192.168.56.101"
PORT = 5000

# PC2 IP address
TARGET = "192.168.10.20"

# Number of ping packets
PACKET_COUNT = 5


def get_live_metrics(duration=15):
    latencies = []
    buffer = ""

    try:
        # Connect to PC1 console
        s = socket.create_connection((HOST, PORT), timeout=5)
        s.settimeout(1)

        # Read and clear any old console output
        time.sleep(0.5)

        try:
            while True:
                old_data = s.recv(4096)
                if not old_data:
                    break
        except socket.timeout:
            pass

        # Send ping command to PC1
        command = f"ping {TARGET} -c {PACKET_COUNT}\n"
        s.sendall(command.encode())

        # Read console output until all replies arrive
        start = time.time()

        while time.time() - start < duration:
            try:
                data = s.recv(4096).decode(errors="ignore")

                if not data:
                    break

                buffer += data

                matches = re.findall(
                    r"time=([\d.]+)\s*ms",
                    buffer
                )

                # Stop after all replies and command prompt return
                if len(matches) >= PACKET_COUNT and "PC1>" in buffer:
                    break

            except socket.timeout:
                continue

        s.close()

        # Extract successful ping times
        matches = re.findall(
            r"time=([\d.]+)\s*ms",
            buffer
        )

        latencies = [float(value) for value in matches[:PACKET_COUNT]]

        successful = len(latencies)
        packet_loss = (
            (PACKET_COUNT - successful) / PACKET_COUNT
        ) * 100

        # Calculate average latency
        average_latency = (
            statistics.mean(latencies) if latencies else 0
        )

        # Calculate jitter
        if len(latencies) > 1:
            jitter = statistics.mean(
                abs(latencies[i] - latencies[i - 1])
                for i in range(1, len(latencies))
            )
        else:
            jitter = 0

        return {
            "status": "Connected",
            "latency": round(average_latency, 3),
            "jitter": round(jitter, 3),
            "packet_loss": round(packet_loss, 2),
            "packets_sent": PACKET_COUNT,
            "successful_replies": successful
        }

    except Exception as e:
        return {
            "status": "Connection Error",
            "error": str(e),
            "latency": 0,
            "jitter": 0,
            "packet_loss": None,
            "packets_sent": PACKET_COUNT,
            "successful_replies": 0
        }


if __name__ == "__main__":
    print("Starting NetGuard AI Live Monitor...")

    result = get_live_metrics()

    print("\nLIVE NETWORK METRICS")
    print("-------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
