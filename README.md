# geopy.jp

geopy.jp is a Python 3 client for several popular geocoding web service.

geopy.jp makes it easy for Python developers to translate addresses, landmarks across the globe from zipcode in **Japan** using third-party data source.

© geopy.jp was refered to [geopy](https://github.com/geopy/geopy) (original)

## Installation
install using pip with:
```sh
pip install geopy.jp
```

Or, [download source archive and install from them.]

```
cd geopy.jp
python setup.py install
```

## Translate
To translate a zipcode to an adress.

```sh
>>> from geopy.location import Location
>>> loc = Location("5300005")
>>> print(loc.address)
{'data': {'address': '大阪市北区中之島', 'fullAddress': '大阪府大阪市北区中之島', 'pref': '大阪府'}, 'code': 200}
>>> invalid_loc = Location("1234567890")
>>> print(loc.address)
{'code': 404, 'message': 'Address not found.'}
```