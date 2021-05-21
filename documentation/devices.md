# Работа с датчиками
Все датчики, такие как кнопка сброса, считыватель карт и qr кодов, работают как отдельные программы. С            основным сервером они общаются по *http*.
## Обработка датчиков
На примере со сканером карт.
Программа запускается в вечном цикле. Далее происходит блокирование главного потока до введения данных. 
Датчики в ОС определяются по определённому порту, к которым можно подключиться и читать их последовательно:
```python
with serial.Serial('/dev/serial0', 9600) as card:
```
Данные читаются посимвольно: 
```python
current_byte = card.read()
```
Так же идет проверка на символ конца строки и на специальный символ начала строки. Символ начала строки игнорируется, а при вводе символа конца строки считывание прекращается: 
```python
while current_byte != b'\x03':
    if current_byte != b'\x02':
```
Так же происходит удаление оставшихся специальных символов, таких как контрольная сумма и прочих:
```python
return str(int(data[2:-2], 16))
```
Далее считанные данные упаковываются в **JSON** и отправляются на сервер (так же происходит задержка в 5 секунд, чтобы избежать повторного считывания данных):
```python
code = get_card_number()
data = {'card': code}
requests.post(CARD_URL, data=json.dumps(data), headers={'Content-Type': 'application/json'})
time.sleep(5)
```

Аналогично реализована работа с другими датчиками.
## Изменение состояния на сервере
Для обработки запросов от датчиков созданы специальные роуты в файле **views/devices_views.py**, например:
```python
@app.route('/devices/card_reader', methods=['POST'])
def card_reader():
    if request.method == 'POST':
        card_json = request.get_json()
        card = card_json['card']
        app.logger.info("Получено значение карты: " + card)
        helper.set_worker(card)
        return 'success', 200
    else:
        abort(400)
```
Основная задача данного метода - это вызов необходимого метода у класса *DeviceHelper*: 
```python
helper.set_worker(card)
```
Данный класс хранит состояние в переменных:
 ```python
worker = ""
qr_code = ""
is_worker_login = False
is_qr_code_input = False
```
При смене состояния сначала проверяется, были ли до этого какие-то данные:
 ```python
if not self.is_worker_login:
```
а потом данные сохраняются:
 ```python
self.worker = worker
self.is_worker_login = True
```
После сохранения проверяется, можно ли открыть какую-либо ячейку:
 ```python
if self.is_ready():
```
 ```python
def is_ready(self):
   return self.is_worker_login and self.is_qr_code_input
```
и по возможности она открывается:
```python
box_number = self.get_box_number()
if box_number != -1:
    open_slot(box_number)
```
и сбрасывается состояние:
 ```python
def reset(self):
    self.is_worker_login = False
    self.is_qr_code_input = False
    self.led.turn_off_all()
```
