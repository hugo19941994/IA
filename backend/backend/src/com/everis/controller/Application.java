/**
 * RESTFul service
 *
 * @author: Jorge de Castro
 * @version: 17/03/2016/A
 * @see <a href = "https://github.com/hugo19941994/CV-Parser" /> Github
 *      repository </a>
 */
package com.everis.controller;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Application se encarga de correr el ejecutable de Spring del proyecto restcvparser
 * @author Jorge de Castro
 *
 */
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
