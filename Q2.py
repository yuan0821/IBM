cont_record=['1 false ERR_OOM','2 true','3 false ERR_TIME_OUT','4 true','5 true']

for cont in cont_record:
  print(cont.split())
  Valid=cont.split()[1]

  if Valid=='false':
    errorCodes=cont.split()[2]
    errorCodes+=errorCodes
    


  if Valid=='true':
    all=+1

if all==len(cont_record):
  print('yes')
else:
  print('NO')
  print(errorCodes)
