# Air time Service.

from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from get_airtime_recipients import recipients

# login credentials
username = "username"
apikey = "apikey"

# Importing Details of airtime receivers
# dicts to hold the recipients and the amount to send
recipients = recipients('employee.csv')

#print recipients

# new instance africa talking gateway class
gateway = AfricasTalkingGateway(username, apikey)

try:
    responses = gateway.sendAirtime(recipients)
    for response in responses:
        print "phoneNumber=%s; amount=%s; status=%s; discount=%s; requestId=%s" % (
            response['phoneNumber'],
            response['amount'],
            response['status'],
            response['discount'],
            response['requestId']
        )
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while sending airtime: %s' % str(e)
