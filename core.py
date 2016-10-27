import os,sys,subprocess
def getFileExtension():
  if(os.name == 'posix'):
    return ''
  else:
    return '.exe'

def runTest(file, input,output):
  os.system(str('fpc '+file))
  try:
    with subprocess.Popen([(str(file.split('.')[0])+getFileExtension())], stdout=subprocess.PIPE,stdin=subprocess.PIPE) as p:
      result = p.communicate(input=input,timeout=1)[0].decode('UTF-8')
      if(str(result)==str(output)):
        eq = True
      else:
        eq = False
      return eq, p
  except FileNotFoundError:
    raise compilationError

