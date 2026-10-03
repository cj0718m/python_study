second=int(input("초를 입력하세요:"))
hour=second//3600
minute=(second%3600)//60
print(hour,"시간",minute,"분",second%60,"초")