# This is a gist
This is such an ugly way to handle data. I hope nobody sees this.


## DNSCrypt Configure
`simple.py` and `filter.py` used to generate the `toml` file.


### Generate certificate request:
'client.pem' is cert request and contains the private key and certificate.
```
openssl req -x509 -out localhost.crt -keyout localhost.key \
  -newkey rsa:4096 -pkeyopt rsa_keygen_pubexp:3 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n \
   [EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth") \
   && cat localhost.key localhost.crt > cert.pem
```


### Download public-resolvers
download text as json object and save as a file.

```
python3 simple.py
```


### Generate configuration
Using filters that I prefer ('DNSCrypt', 'DNSSEC' and nolog and nofilter enabled).

```
python3 filter.py
```

## magic prime sieve  
Calculate (very fast) primes in range and slowly print. 
~30 seconds to print 1M (no I didn't create the sieve)

`python3 numb.py <range>`

## walk.py
crawl 'https://www.example.com'

`python3 walk.py`


__needs to behave less spidery and walk only on the seeded url.__


#### MISC
download encoded text in json format. 
i had to give up on my attempt to do this with pure sockets because
the buffer was full and continuation was not something i can figure out :(.

###### BOM
byte order marks. this unicode escape sequence of characters indicates byte order
change in a stream of bytes.
```
 sed -e '1s/^\xef\xbb\xbf//' < bomfile > newfile
```


# GIFIF
Request for Information

## TODO:
1. standard io for interchange domain
2. method for platform conformity
3. eventually:
- BREAK IO
- GOTO STEP 1
4. eventually:
- TRUST IO
- yeah, i think so


![Pascal's Triangle](https://github.com/jradd/public/blob/master/pascals.gif)
