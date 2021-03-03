# DO DNS API

REST API to create a DNS record.

## Setup
Deploy to app platform. Set the following environment variables

* `DO_TOKEN` - A DigitalOcean API Token with write access
* `DOMAIN` - A domain registered with DigitalOcean that the token can create records for
* `PASSWORD` - A password users must enter to create a DNS record

## Usage

`/` POST

```
{
    "password": SERVER_PASSWORD,
    "name": SUBDOMAIN_NAME,
    "ip": IPV4_ADDRESS
}
```