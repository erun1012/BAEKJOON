import sys

C_dic = {"NLCS": "North London Collegiate School", "BHA": "Branksome Hall Asia", "KIS": "Korea International School", "SJA": "St. Johnsbury Academy"}

S = str(sys.stdin.readline().rstrip())

print(C_dic[S])