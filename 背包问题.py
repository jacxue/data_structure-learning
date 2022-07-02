# -*- coding:utf-8 -*-
# 作者：薛晓通

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = []

if __name__ == "__main__":
    while states_needed:
        best_station = None
        states_coverd = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_coverd):
                best_station = station
                states_coverd = covered
        states_needed -= states_coverd
        final_stations.append(best_station)
    print(final_stations)