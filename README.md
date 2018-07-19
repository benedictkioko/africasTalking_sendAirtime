## africasTalking_sendAirtime API

clone the directory and run

```
$ python send_airtime.py
```

### `AirtimeService`

- `send(phone_number: str, amount: str)`: Send airtime to a phone number. An example amount would be `KES 150`.

```python
import africastalking
africastalking.initialize(username='sandbox', api_key='someKey')
airtime = africastalking.Airtime
res = airtime.send(phone_number='+254718769882', amount='KES 908')
```

- `send(recipients: [dict])`: Send airtime to a list of phone numbers. The keys in the `recipients` dictionary are phone numbers while the values are airtime amounts. The amounts need to have currency info e.g. `UXG 4265`.

```python
import africastalking
africastalking.initialize(username='sandbox', api_key='someKey')
airtime = africastalking.Airtime
res = airtime.send(recipients=[
            {'phoneNumber': '+2348160663047', 'amount': 'NGN 1535' },
            {'phoneNumber': '+254718769881', 'amount': 'KES 733'},
])
```

For more information about status notification, please read [http://docs.africastalking.com/airtime/callback](http://docs.africastalking.com/airtime/callback)
