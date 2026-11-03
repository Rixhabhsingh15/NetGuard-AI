
TROUBLESHOOTING = {
    "Normal": {
        "cause": "Network is operating normally.",
        "solution": "No action required. Continue monitoring network performance."
    },

    "Congestion": {
        "cause": "High network traffic is consuming available bandwidth.",
        "solution": "Reduce unnecessary traffic, increase bandwidth, or apply traffic management and QoS."
    },

    "Link_Failure": {
        "cause": "The network link may be disconnected or unavailable.",
        "solution": "Check Ethernet cables, interfaces, switches, and link status."
    },

    "Device_Overload": {
        "cause": "CPU or memory utilization of the network device is too high.",
        "solution": "Reduce device workload, investigate high-resource processes, or upgrade device resources."
    },

    "Routing_Issue": {
        "cause": "Incorrect or inefficient routing configuration.",
        "solution": "Check routing tables, gateway configuration, and routing protocols."
    },

    "High Latency": {
        "cause": "Network congestion, long routing path, or poor connectivity.",
        "solution": "Check network congestion, reduce background traffic, and verify routing."
    },

    "Packet Loss": {
        "cause": "Unstable connection, faulty link, interference, or congestion.",
        "solution": "Check cables, network interfaces, and congestion."
    },

    "High Jitter": {
        "cause": "Variable network delay caused by congestion or unstable connectivity.",
        "solution": "Reduce network traffic and check network stability."
    }
}


def get_recommendation(fault):
    return TROUBLESHOOTING.get(
        str(fault),
        {
            "cause": "The system detected an abnormal network condition.",
            "solution": "Check latency, packet loss, jitter, bandwidth, and device resource utilization."
        }
    )
