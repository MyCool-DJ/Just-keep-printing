# Secret Three: Cursor

David, you muppet! Why are we doing this again? We already learned this...

👉 Do you notice how difficult this is to read?
```python
import os

for i in range(1, 101):
  print(i)
  os.system("clear")
```

Your probably thinking...David, `import time`:

👉 Let's do it, but is there anything you still notice?

```python
import os, time

for i in range(1, 101):
  print(i)
  time.sleep(0.5)
  os.system("clear")
```


## That GIANT white cursor...

I bet you didn't even know we could turn that off! It is just a sneaky `print` command.

![](resources/cursor_off.png)

👉 Let's try the same code, but turn the cursor off:

```python
import os, time
print('\033[?25l', end="")
for i in range(1, 101):
  print(i)
  time.sleep(0.2)
  os.system("clear")
```
What if we want to turn the cursor back on:

![](resources/cursor_on.png)