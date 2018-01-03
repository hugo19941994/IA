# CV Parser

| Python | Java |
|--------|------|
| [![Requirements Status](https://requires.io/github/hugo19941994/cv-parser/requirements.svg?branch=master)](https://requires.io/github/hugo19941994/cv-parser/requirements/?branch=master) | [![Dependency Status](https://beta.gemnasium.com/badges/github.com/hugo19941994/cv-parser.svg)](https://beta.gemnasium.com/projects/github.com/hugo19941994/cv-parser) |

## Deployment

Install Docker and docker-compose.

Replace the `URL` variable in `./config/conf.env` with the actual URL which will be used.

The other variables can also be modified:
* `DBUSR`: User for MariaDB
* `DBPWD`: Password for MariaDB
* `CVUSR`: Website's administrator user
* `CVPWD`: Website's administrator password

For MariaDB's root user a random password will be generated with OpenSSL.

Run a reverse proxy such as Nginx on port 3020. You can change this port in `docker-compose.yml`.

To run the app simply

```bash
$ docker-compose up -d
```
