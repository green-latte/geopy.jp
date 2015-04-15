import urllib.request
import json

class Location():
  LANG = "ja"
  def __init__(self, zipcode):
    # substring '-'
    if isinstance(zipcode, int):
      self.zipcode = str(zipcode)
    else:
      self.zipcode = zipcode

  @property
  def address(self):
    params = "zipcode={0}&lang={1}".format(self.zipcode, self.LANG)
    req = urllib.request.Request('http://api.zipaddress.net/?{0}'.format(params))
    res = urllib.request.urlopen(req)
    return json.loads(res.read().decode('utf-8'))