def compute_tcp_congestion_time(con_win, MSS, RTT):
    RTT_COUNT = 1
    MSS_COUNT = 1

    while (MSS_COUNT * MSS < con_win):
        print(f"RTT: {RTT_COUNT}, # MSS: {MSS_COUNT} | {MSS_COUNT * MSS}")
        MSS_COUNT = MSS_COUNT * MSS
        RTT_COUNT += 1
    
    if (MSS_COUNT * MSS == con_win):
        print(f"RTT: {RTT_COUNT}, # MSS: {MSS_COUNT} | {MSS_COUNT * MSS}")
        return RTT_COUNT * RTT
    else:
        return "Failed"

RTT = 100    # ms
MSS = 2      # kb
con_win = 32 # kb

print("Time: ", compute_tcp_congestion_time(con_win, MSS, RTT))
