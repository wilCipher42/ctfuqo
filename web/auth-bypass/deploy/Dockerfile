FROM php:8.1-apache

WORKDIR /var/www/html

# copy site files
COPY src/ /var/www/html/

# basic permissions
RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html

